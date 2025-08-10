#include <iostream>
using namespace std;

int main() {
  int test_cases;
  cin >> test_cases;
  for (int test_case = 0; test_case < test_cases; test_case++) {
    int n;
    cin >> n;
    int a[n], b[n];
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
      cin >> b[i];
    }
    // for (int i = 0; i >= 0; i--) {
    //   if ((a[i] ^ a[i + 1]) == b[i]) {
    //     a[i] = (a[i] ^ a[i + 1]);
    //   }
    // }
    // for (int i = n - 2; i >= 0; i--) {
    //   if ((a[i] ^ a[i + 1]) == b[i]) {
    //     a[i] = (a[i] ^ a[i + 1]);
    //   }
    // }
    bool change = true;
    while (change) {
      change = false;
      for (int i = 0; i < n-1; i++) {
        if (a[i] != b[i] && (a[i] ^ a[i + 1]) == b[i]) {
          a[i] = a[i] ^ a[i+1];
          change = true;
        }
      }
    }
    bool solved = true;
    for (int i = 0; i < n; i++) {
      if (a[i] != b[i]) {
        solved = false;
        break;
      }
    }
    if (solved) {
      cout << "YES" << "\n";
    } else {
      cout << "NO" << "\n";
      // for (int i = 0; i < n; i++) {
      //   cout << a[i] << " ";
      // }
      // cout << "\n";
      // for (int i = 0; i < n; i++) {
      //   cout << b[i] << " ";
      // }
    }
  }
  return 0;
}
