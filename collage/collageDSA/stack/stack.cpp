#include <iostream>
using namespace std;

class Stack {
private:
  int top;
  int stack[10];

public:
  Stack() { top = 0; }
  int peek() { return stack[top - 1]; }
  int pop() {
    if (top == 0) {
      cout << "Stack underflow";
      return 0;
    }
    top--;
    return stack[top];
  }
  void push(int ele) {
    if (top == 10 - 1) {
      cout << "Stack overflow";
      return;
    }
    stack[top] = ele;
    top++;
  }
  bool empty() {
    if (top == 0) {
      return true;
    }
    return false;
  }
  void trav() {
    for (int i = 0; i < top; i++) {
      cout << stack[i] << " ";
    }
    cout << endl;
  }
};

int main() {
  Stack s;
  cout << "Pushing 1" << endl;
  s.push(1);
  cout << "Pushing 20" << endl;
  s.push(20);
  cout << "Pushing 25" << endl;
  s.push(25);
  cout << "Peeking into stack: ";
  cout << s.peek() << endl;
  cout << "Is stack empty: ";
  if (s.empty()) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
  cout << "Popping once" << endl;
  s.pop();
  cout << "Popping twice" << endl;
  s.pop();
  cout << "Traversing stack" << endl;
  s.trav();
  return 0;
}
