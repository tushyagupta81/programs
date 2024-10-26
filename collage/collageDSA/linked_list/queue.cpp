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

class Queue {
private:
  Node *head;
  Node *tail;

public:
  Queue() {
    head = NULL;
    tail = NULL;
  }
  void enque(int v) {
    Node *nn = new Node(v);
    if (head == NULL) {
      head = nn;
      tail = nn;
    } else {
      tail->next = nn;
      tail = nn;
    }
  }
  void deque() {
    if (head == NULL) {
      cout << "Queue underflow" << endl;
      return;
    }
    if (head == tail) {
      Node *r = head;
      head = NULL;
      tail = NULL;
      free(r);
      return;
    }
    Node *r = head;
    head = head->next;
    free(r);
  }
  void trav() {
    if (head == NULL) {
      cout << "Queue is empty" << endl;
      return;
    }
    Node *n = head;
    while (n->next != NULL) {
      cout << n->val << "<-";
      n = n->next;
    }
    cout << n->val << endl;
  }
};

int main() {
  Queue q;
  q.enque(5);
  q.enque(10);
  q.enque(15);
  q.trav();
  q.deque();
  q.deque();
  q.deque();
  q.trav();
  q.enque(5);
  q.enque(10);
  q.enque(15);
  q.enque(20);
  q.trav();
  q.deque();
  q.deque();
  q.trav();
  q.enque(25);
  q.enque(30);
  q.trav();

  return 0;
}
