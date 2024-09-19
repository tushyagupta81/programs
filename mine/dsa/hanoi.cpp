#include <iostream>
using namespace std;

void pm(int start, int end) { cout << start << "->" << end << endl; }

void h(int size, int start, int end) {
  if (size == 1) {
    pm(start, end);
  } else {
    int other = 6 - (start + end);
    h(size - 1, start, other);
    pm(start, end);
    h(size - 1, other, end);
  }
}

int main() {
  h(8, 1, 3);

  return 0;
}
