#include <iostream>
using namespace std;

class Node {
public:
  int val;
  Node *next;
  Node(int a) {
    this->val = a;
    this->next = NULL;
  }
};

class SLL {
private:
  Node *root;

public:
  SLL() { this->root = NULL; }
  void insert(int v) {
    if (root == NULL) {
      Node *nn = new Node(v);
      root = nn;
      return;
    }
    Node *n = root;
    while (n->next != NULL) {
      n = n->next;
    }
    Node *nn = new Node(v);
    n->next = nn;
  }
  void rev() {
    if (root == NULL) {
      return;
    } else if (root->next == NULL) {
      return;
    } else if (root->next->next == NULL) {
      Node *n1 = root;
      Node *n2 = root->next;
      n2->next = n1;
      n1->next = NULL;
      root = n2;
      return;
    }
    Node *past = NULL;
    Node *cur = root;
    Node *future = root->next;
    while (cur != NULL) {
      if (cur->next == NULL) {
        root = cur;
      }
      cur->next = past;
      past = cur;
      cur = future;
      if (future != NULL) {
        future = future->next;
      }
    }
  }
  void trav() {
    Node *n = root;
    while (n->next != NULL) {
      cout << n->val << "->";
      n = n->next;
    }
    cout << n->val << endl;
  }
};

int main() {
  int c;
  cout << "Enter number of elements: ";
  cin >> c;
  SLL l;
  int a;
  for (int i = 0; i < c; i++) {
    cin >> a;
    l.insert(a);
  }
  l.trav();
  l.rev();
  l.trav();

  return 0;
}
