#include <iostream>
using namespace std;

int main() {
  int test_cases;
  cin >> test_cases;
  for (int k = 0; k < test_cases; k++) {
    int n;
    cin >> n;
    for (int i = 0; i < n - 1; i++) {
      if (i % 2 == 0) {
        cout << -1 << " ";
      } else {
        cout << 3 << " ";
      }
    }
    if (n % 2 == 0) {
      cout << 2 << "\n";
    } else {
      cout << -1 << "\n";
    }
  }
}
