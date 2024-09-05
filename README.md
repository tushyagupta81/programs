``` bash
git clone --recurse-submodules -j8 git@github.com:tushyagupta81/programs.git
cd programs
git submodule foreach "git checkout main || git checkout master || :"
```
to clone and shift branches back to main
