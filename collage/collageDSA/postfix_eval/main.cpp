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

int main() {
  string postfix;
  getline(cin, postfix);
  Stack s;
  unordered_map<string, int> pred;
  pred["-"] = 0;
  pred["+"] = 1;
  pred["/"] = 2;
  pred["*"] = 3;
  pred["^"] = 4;
  regex delim("\\s+");
  sregex_token_iterator tokenIterator(postfix.begin(), postfix.end(), delim,
                                      -1);
  sregex_token_iterator endIterator;
  while (tokenIterator != endIterator) {
    string sy = *tokenIterator;
    if (pred.count(sy) == 0) {
      s.push(sy);
    } else {
      float op_2 = stof(s.pop());
      float op_1 = stof(s.pop());
      float value;
      int v = pred[sy];
      if (v == 0) {
        value = op_1 - op_2;
      } else if (v == 1) {
        value = op_1 + op_2;
      } else if (v == 2) {
        value = op_1 / op_2;
      } else if (v == 3) {
        value = op_1 * op_2;
      } else if (v == 4) {
        value = pow(op_1, op_2);
      }
      s.push(to_string(value));
    }
    ++tokenIterator;
  }
  string result = s.pop();
  cout << result;
  return 0;
}
