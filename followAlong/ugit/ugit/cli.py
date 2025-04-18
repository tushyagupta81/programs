import argparse
import platform
import tempfile
import subprocess
import textwrap
import os
import sys

from ugit import data
from ugit import base


def main():
    args = parse_args()
    args.func(args)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest="command")
    commands.required = True

    oid = base.get_oid

    init_parser = commands.add_parser("init")
    init_parser.set_defaults(func=init)

    hash_object_parser = commands.add_parser("hash-object")
    hash_object_parser.set_defaults(func=hash_object)
    hash_object_parser.add_argument("file")

    cat_file_parser = commands.add_parser("cat-file")
    cat_file_parser.set_defaults(func=cat_file)
    cat_file_parser.add_argument("object_hash", type=oid)

    write_tree_parser = commands.add_parser("write-tree")
    write_tree_parser.set_defaults(func=write_tree)

    read_tree_parser = commands.add_parser("read-tree")
    read_tree_parser.set_defaults(func=read_tree)
    read_tree_parser.add_argument("tree", type=oid)

    commit_parser = commands.add_parser("commit")
    commit_parser.set_defaults(func=commit)
    commit_parser.add_argument("-m", "--message", required=True)

    log_parser = commands.add_parser("log")
    log_parser.set_defaults(func=log)
    log_parser.add_argument("oid", default="@", type=oid, nargs="?")

    checkout_parser = commands.add_parser("checkout")
    checkout_parser.set_defaults(func=checkout)
    checkout_parser.add_argument("commit")

    tag_parser = commands.add_parser("tag")
    tag_parser.set_defaults(func=tag)
    tag_parser.add_argument("name")
    tag_parser.add_argument("oid", default="@", type=oid, nargs="?")

    branch_parser = commands.add_parser("branch")
    branch_parser.set_defaults(func=branch)
    branch_parser.add_argument("name", nargs="?")
    branch_parser.add_argument("start_point", default="@", type=oid, nargs="?")

    k_parser = commands.add_parser("k")
    k_parser.set_defaults(func=k)

    status_parser = commands.add_parser("status")
    status_parser.set_defaults(func=status)

    reset_parser = commands.add_parser("reset")
    reset_parser.set_defaults(func=reset)
    reset_parser.add_argument("commit", type=oid)

    return parser.parse_args()


def init(_):
    base.init()
    print(f"Initialized empty ugit repository in {os.getcwd()}/{data.GIT_DIR}")


def hash_object(args):
    with open(args.file, "rb") as f:
        print(data.hash_object(f.read()))


def cat_file(args):
    sys.stdout.flush()
    sys.stdout.buffer.write(data.get_contents(args.object_hash, expected=None))


def write_tree(_):
    print(base.write_tree())


def read_tree(args):
    base.read_tree(args.tree)


def commit(args):
    print(base.commit(args.message))


def log(args):
    refs = {}
    for refname, ref in data.iter_refs():
        refs.setdefault(ref.value, []).append(refname)

    for oid in base.iter_commits_and_parents({args.oid}):
        commit = base.get_commit(oid)

        refs_str = f" ({', '.join(refs[oid])})" if oid in refs else ""
        print(f"commit {oid}{refs_str}")
        print(textwrap.indent(commit.message, "  "))
        print("")


def checkout(args):
    base.checkout(args.commit)


def tag(args):
    base.create_tag(args.name, args.oid)


def k(_):
    dot = "digraph commits{\n"

    oids = set()
    for refname, ref in data.iter_refs(deref=False):
        dot += f'"{refname}" [shape=note]\n'
        dot += f'"{refname}" -> "{ref.value}"\n'
        if not ref.symbolic:
            oids.add(ref.value)

    for oid in base.iter_commits_and_parents(oids):
        commit = base.get_commit(oid)
        dot += (
            f'"{oid}" [shape=box style=filled label="{oid[:10]}\n{commit.message}"]\n'
        )
        if commit.parent:
            dot += f'"{oid}" -> "{commit.parent}"\n'

    dot += "}"

    with subprocess.Popen(
        ["dot", "-Tjpeg", "-Gdpi=300"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ) as proc:
        output, error = proc.communicate(dot.encode())

    if proc.returncode != 0:
        print("Graphviz error:", error.decode())
    else:
        # Save to a temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(output)
            tmp_path = tmp.name

        # Open with default image viewer
        if platform.system() == "Darwin":  # macOS
            subprocess.run(["open", tmp_path])
        elif platform.system() == "Linux":
            subprocess.run(["xdg-open", tmp_path])
        else:
            print(
                f"Don't know how to open files on {platform.system()}. File saved to: {tmp_path}"
            )


def branch(args):
    if not args.name:
        current = base.get_branch_name()
        for branch in base.iter_branch_name():
            prefix = "*" if branch == current else " "
            print(f"{prefix} {branch}")
    else:
        base.create_branch(args.name, args.start_point)
        print(f"Branch {args.name} created at {args.start_point[:10]}")


def status(_):
    HEAD = base.get_oid("@")
    branch = base.get_branch_name()
    if branch:
        print(f"On branch {branch}")
    else:
        print(f"HEAD detached at {HEAD[:10]}")

def reset(args):
    base.reset(args.commit)
