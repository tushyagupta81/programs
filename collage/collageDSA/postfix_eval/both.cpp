#include <iostream>
#include <math.h>
#include <regex>
#include <string.h>
#include <unordered_map>
using namespace std;

class Stack {
private:
  int top;
  string stack[10];

public:
  Stack() { top = 0; }
  string peek() { return stack[top]; }
  string pop() {
    top--;
    return stack[top + 1];
  }
  void push(string ele) {
    stack[top + 1] = ele;
    top++;
  }
  bool empty() {
    if (top == 0) {
      return true;
    }
    return false;
  }
};

bool com_pred(char top, char curr, unordered_map<char, int> pred) {
  if (top == '(') {
    return false;
  }
  if (pred[top] >= pred[curr]) {
    return true;
  }
  return false;
}

int main() {
  unordered_map<char, int> pred;
  pred['-'] = 1;
  pred['+'] = 1;
  pred['/'] = 2;
  pred['*'] = 2;
  pred['^'] = 3;
  pred['('] = 4;
  string infix;
  cin >> infix;
  string postfix;
  Stack s;
  for (int i = 0; i < infix.size(); i++) {
    char sy = infix[i];
    if (sy == ')') {
      while (s.peek() != '(') {
        postfix += s.pop();
      }
      s.pop();
    } else {
      if (!pred[sy]) {
        postfix += sy;
      } else {
        while (!s.empty() && com_pred(s.peek(), sy, pred)) {
          char t = s.pop();
          postfix += t;
        }
        s.push(sy);
      }
    }
  }
  while (!s.empty()) {
    postfix += s.pop();
  }
  cout << postfix;
  return 0;
}
