#include <iostream>
using namespace std;

class Node {
public:
  int val;
  int height;
  int bal_fac;
  Node *left;
  Node *right;
  Node *parent;
  Node() {
    height = 0;
    bal_fac = 0;
    left = NULL;
    right = NULL;
    parent = NULL;
  }
  Node(int a) {
    val = a;
    height = 0;
    bal_fac = 0;
    left = NULL;
    right = NULL;
    parent = NULL;
  }
};

class AVL {
private:
  Node *root;
  void insert(int a, Node *node) {
    if (node->val > a) {
      if (node->left == NULL) {
        Node *nn = new Node(a);
        node->left = nn;
        nn->parent = node;
        int c = 1;
        while (nn->parent != NULL) {
          nn->parent->height =
              (nn->parent->height > c ? nn->parent->height : c);
          c += 1;
          nn->parent->bal_fac =
              (nn->parent->left != NULL ? nn->parent->left->height : -1) -
              (nn->parent->right != NULL ? nn->parent->right->height : -1);
          nn = nn->parent;
        }
        return;
      }
      insert(a, node->left);
    } else if (node->val <= a) {
      if (node->right == NULL) {
        Node *nn = new Node(a);
        node->right = nn;
        nn->parent = node;
        int c = 1;
        while (nn->parent != NULL) {
          nn->parent->height =
              (nn->parent->height > c ? nn->parent->height : c);
          c += 1;
          nn->parent->bal_fac =
              (nn->parent->left != NULL ? nn->parent->left->height : -1) -
              (nn->parent->right != NULL ? nn->parent->right->height : -1);
          nn = nn->parent;
        }
        return;
      }
      insert(a, node->right);
    }
  }
  void printBT(const std::string &prefix, const Node *node, bool isLeft) {
    if (node != NULL) {
      cout << prefix;

      cout << (isLeft ? "├──" : "└──");

      // print the value of the node
      cout << node->val << " " << node->height << " " << node->bal_fac << endl;

      // enter the next tree level - left and right branch
      printBT(prefix + (isLeft ? "│   " : "    "), node->left, true);
      printBT(prefix + (isLeft ? "│   " : "    "), node->right, false);
    }
  }
  void printBT(const Node *node) { printBT("", node, false); }

public:
  AVL() { root = NULL; }
  void insert(int a) {
    if (root == NULL) {
      Node *nn = new Node(a);
      root = nn;
      return;
    }
    insert(a, root);
  }
  void dis() { printBT(root); }
};

int main() {
  AVL b;
  int a[10] = {3, 5, 1, 2, 6, 4, 8, 7, 9, 0};
  for (int j = 0; j < 10; j++) {
    b.insert(a[j]);
    cout << endl;
    b.dis();
    cout << endl;
  }
  return 0;
}
