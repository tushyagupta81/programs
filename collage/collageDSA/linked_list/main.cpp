#include <iostream>
using namespace std;

class Node {
public:
  int val;
  Node *next;
  Node() { next = NULL; }
  Node(int v) {
    val = v;
    next = NULL;
  }
};

class SLL {
private:
  Node *start;

public:
  SLL() { start = NULL; }
  void insert_begin(int v) {
    Node *nn = new Node(v);
    nn->next = start;
    start = nn;
  }
  void insert_end(int v) {
    if (start == NULL) {
      this->insert_begin(v);
      return;
    }
    Node *nn = new Node(v);
    Node *temp = start;
    while (temp->next != NULL) {
      temp = temp->next;
    }
    temp->next = nn;
  }
  void insert_after(int loc, int v) {
    Node *nn = new Node(v);
    Node *temp = start;
    for (int i = 0; i < loc - 1; i++) {
      if (temp == NULL) {
        cout << "Location out of length of SLL" << endl;
        return;
      }
      temp = temp->next;
    }
    if (temp == NULL) {
      cout << "Location out of length of SLL" << endl;
      return;
    } else {
      nn->next = temp->next;
      temp->next = nn;
    }
  }
  void insert_before(int loc, int v) {
    if (loc == 1) {
      this->insert_begin(v);
      return;
    }
    Node *nn = new Node(v);
    Node *temp = start;
    Node *prev;
    for (int i = 0; i < loc - 1; i++) {
      if (temp == NULL) {
        cout << "Location out of length of SLL" << endl;
        return;
      }
      prev = temp;
      temp = temp->next;
    }
    if (temp == NULL) {
      cout << "Location out of length of SLL" << endl;
      return;
    } else {
      nn->next = temp;
      prev->next = nn;
    }
  }
  void delete_begin() {
    if (start != NULL) {
      Node *r = start;
      start = start->next;
      free(r);
    } else {
      cout << "List has no elements" << endl;
    }
  }
  void delete_end() {
    if (start == NULL) {
      cout << "List is empty" << endl;
      return;
    }
    if (start->next == NULL) {
      Node *r = start;
      start = NULL;
      free(r);
      return;
    }
    Node *temp = start;
    Node *prev;
    while (temp->next != NULL) {
      prev = temp;
      temp = temp->next;
    }
    prev->next = NULL;
    free(temp);
  }
  void del(int r) {
    if (start == NULL) {
      cout << "List empty" << endl;
      return;
    }
    if (start->val == r) {
      this->delete_begin();
      return;
    }
    Node *temp = start;
    Node *prev;
    while (temp->next != NULL && temp->val != r) {
      prev = temp;
      temp = temp->next;
    }
    if (temp->val == r) {
      if (temp == start) {
        start = start->next;
        return;
      }
      prev->next = temp->next;
      free(temp);
    } else {
      cout << "Node not found" << endl;
    }
  }
  void display() {
    Node *temp = start;
    while (temp != NULL) {
      cout << temp->val << " -> ";
      temp = temp->next;
    }
    cout << "NULL" << endl;
  }
};

int main() {
  SLL l;
  cout << "Inserting 5 to 9 in reverse order at begining\n";
  l.insert_begin(5);
  l.insert_begin(6);
  l.insert_begin(7);
  l.insert_begin(8);
  l.insert_begin(9);
  l.display();
  cout << "Inserting 10 at the end\n";
  l.insert_end(10);
  l.display();
  cout << "Deleting 2 at begining and ending each\n";
  l.delete_begin();
  l.delete_begin();
  l.delete_end();
  l.delete_end();
  l.display();
  cout << "Inserting 11 after 2\n";
  l.insert_after(2, 11);
  l.display();
  cout << "Inserting 12 after 3\n";
  l.insert_after(3, 12);
  l.display();
  cout << "Inserting 13 before 1\n";
  l.insert_before(1, 13);
  l.display();
  cout << "Inserting 14 before 2\n";
  l.insert_before(2, 14);
  l.display();
  cout << "Deleting over the limit\n";
  l.delete_end();
  l.delete_end();
  l.delete_end();
  l.delete_end();
  l.delete_end();
  l.delete_end();
  l.delete_end();
  l.delete_end();
  l.display();
  cout << "Inserting 10 at end\n";
  l.insert_end(10);
  l.display();
  cout << "Inserting 32 at begining\n";
  l.insert_begin(32);
  l.display();
  cout << "Deleting over the limit\n";
  l.delete_begin();
  l.delete_begin();
  l.delete_begin();
  l.display();
  cout << "Inserting 10 before 1\n";
  l.insert_before(1, 10);
  l.display();
  cout << "Inserting 5 to 9 in reverse order at begining\n";
  l.insert_begin(5);
  l.insert_begin(6);
  l.insert_begin(7);
  l.insert_begin(8);
  l.insert_begin(9);
  l.display();
  cout << "Deleting node 5, 6 and 7\n";
  l.del(5);
  l.del(6);
  l.del(7);
  l.display();

  return 0;
}
