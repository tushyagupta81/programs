#include <iostream>
using namespace std;

class Node {
public:
  int val;
  Node *left;
  Node *right;
  Node *parent;
  Node() {
    left = NULL;
    right = NULL;
    parent = NULL;
  }
  Node(int a) {
    val = a;
    left = NULL;
    right = NULL;
    parent = NULL;
  }
};
class BST {
private:
  Node *root;
  void printBT(const std::string &prefix, const Node *node, bool isLeft) {
    if (node != NULL) {
      cout << prefix;

      cout << (isLeft ? "├──" : "└──");

      // print the value of the node
      cout << node->val << endl;

      // enter the next tree level - left and right branch
      printBT(prefix + (isLeft ? "│   " : "    "), node->left, true);
      printBT(prefix + (isLeft ? "│   " : "    "), node->right, false);
    }
  }
  void printBT(const Node *node) { printBT("", node, false); }
  Node *max_node(Node *node) {
    if (node->right != NULL) {
      return max_node(node->right);
    } else {
      return node;
    }
  }
  Node *min_node(Node *node) {
    if (node->left != NULL) {
      return max_node(node->left);
    } else {
      return node;
    }
  }
  void insert(int a, Node *node) {
    if (node->val > a) {
      if (node->left == NULL) {
        Node *nn = new Node(a);
        node->left = nn;
        nn->parent = node;
        return;
      }
      insert(a, node->left);
    } else if (node->val <= a) {
      if (node->right == NULL) {
        Node *nn = new Node(a);
        node->right = nn;
        nn->parent = node;
        return;
      }
      insert(a, node->right);
    }
  }
  void del_node(Node *node) {
    if (node->left == NULL && node->right == NULL) {
      if (node->val > node->parent->val) {
        node->parent->right = NULL;
      } else {
        node->parent->left = NULL;
      }
      free(node);
    } else if (node->left != NULL) {
      Node *max = max_node(node->left);
      node->val = max->val;
      if (max->left == NULL) {
        if (max->parent == node) {
          max->parent->left = NULL;
        } else {
          max->parent->right = NULL;
        }
        free(max);
      } else {
        del_node(max);
      }
    } else if (node->left == NULL && node->right != NULL) {
      Node *min = min_node(node->right);
      node->val = min->val;
      if (min->right == NULL) {
        if (min->parent == node) {
          min->parent->right = NULL;
        } else {
          min->parent->left = NULL;
        }
        free(min);
      } else {
        del_node(min);
      }
    }
  }

public:
  BST() { root = NULL; }
  void insert(int a) {
    if (root == NULL) {
      Node *nn = new Node(a);
      root = nn;
      return;
    }
    insert(a, root);
  }
  void dis() { printBT(root); }
  void find_and_del(int a) {
    Node *node = root;
    while (node->val != a) {
      if (node->val > a) {
        node = node->left;
      } else {
        node = node->right;
      }
      if (node == NULL) {
        cout << "Node not found" << endl;
        return;
      }
    }
    del_node(node);
  }
};

int main() {
  BST b;
  int i, c = 0;
  int a[10] = {3, 5, 1, 2, 6, 4, 8, 7, 9, 0};
  while (true) {
    cout << "Choose one of the following:\n";
    cout << "0. Exit\n";
    cout << "1. Insert a element\n";
    cout << "2. Delete a element\n";
    cout << "3. Enter precreated 10 elements\n";
    cout << "-> ";
    cin >> c;
    switch (c) {
    case 0:
      return 0;
    case 1:
      cout << "\nEnter number to insert: ";
      cin >> i;
      b.insert(i);
      cout << endl;
      b.dis();
      cout << endl;
      break;
    case 2:
      cout << "\nEnter number to delete: ";
      cin >> i;
      b.find_and_del(i);
      cout << endl;
      b.dis();
      cout << endl;
      break;
    case 3:
      for (int j = 0; j < 10; j++) {
        b.insert(a[j]);
      }
      cout << endl;
      b.dis();
      cout << endl;
      break;
    default:
      continue;
    }
  }
  return 0;
}
