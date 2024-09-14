#include <iostream>
using namespace std;

#define MAX 10

class CirQueue {
private:
  int front;
  int rear;
  int arr[MAX];

public:
  CirQueue() { front = rear = -1; }
  void insert(int x) {
    if ((front == 0 && rear == MAX - 1) || (rear + 1 == front)) {
      cout << "Queue overflow" << endl;
    } else if (front == -1) {
      front = rear = 0;
      arr[rear] = x;
    } else if (rear != MAX - 1) {
      rear++;
      arr[rear] = x;
    } else if (front != 0, rear == MAX - 1) {
      rear = 0;
      arr[rear] = x;
    }
  }
  void del() {
    if (front == -1) {
      cout << "Queue underflow" << endl;
    } else if (front != -1 && front == rear) {
      front = rear = -1;
    } else if (front != -1 && front == MAX - 1) {
      front = 0;
    } else {
      front++;
    }
  }
};

int main() {
  CirQueue q;
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
  q.del();
  q.insert(5);
  q.insert(5);
  return 0;
}
