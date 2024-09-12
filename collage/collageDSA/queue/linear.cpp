#include <iostream>
using namespace std;

#define MAX 10

class Queue {
private:
  int front;
  int rear;
  int arr[MAX];

public:
  Queue() { front = rear = -1; }
  void insert(int x) {
    if (rear >= MAX - 1) {
      cout << "Queue overflow" << endl;
    } else if (rear == -1) {
      front = rear = 0;
      arr[rear] = x;
    } else {
      rear++;
      arr[rear] = x;
    }
  }
  void del() {
    if (front == -1) {
      cout << "Queue underflow" << endl;
    } else if (front == rear) {
      front = rear = -1;
    } else {
      front++;
    }
  }
};

int main() {
  Queue q;
  q.del();
  q.insert(5);
  q.insert(10);
  q.del();
  q.del();
  q.del();
  cout << "Inserting 10 elements" << endl;
  q.insert(5);
  q.insert(5);
  q.insert(5);
  q.insert(5);
  q.insert(5);
  q.insert(5);
  q.insert(5);
  q.insert(5);
  q.insert(5);
  q.insert(5);
  cout << "Inserting 11th element" << endl;
  q.insert(5);
  return 0;
}
