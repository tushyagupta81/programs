#include <iostream>
using namespace std;

class Node {
public:
  Node() { this->next = NULL; }
  Node(int v) {
    this->val = v;
    this->next = NULL;
  }
  int val;
  Node *next;
};

class Stack {
private:
  Node *start;

public:
  Stack() { start = NULL; }
  void push(int v) {
    Node *nn = new Node(v);
    nn->next = start;
    start = nn;
  }
  void pop() {
    if (start == NULL) {
      cout << "Stack underflow" << endl;
      return;
    }
    Node *r = start;
    start = start->next;
    free(r);
  }
  int top() {
    if (start == NULL) {
      cout << "Stack empty" << endl;
      return 0;
    }
    return start->val;
  }
};

int main() {
  Stack s;
  s.push(5);
  s.push(6);
  s.push(7);
  s.push(8);
  cout << s.top() << endl;
  s.pop();
  cout << s.top() << endl;
  s.pop();
  cout << s.top() << endl;
  s.pop();
  cout << s.top() << endl;
  s.pop();
  s.pop();
  return 0;
}
