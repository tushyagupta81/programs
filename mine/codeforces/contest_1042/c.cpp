#include <cstdlib>
#include <iostream>
using namespace std;

int main() {
  int test_cases;
  cin >> test_cases;
  for (int test_case = 0; test_case < test_cases; test_case++) {
    int n, k;
    cin >> n;
    cin >> k;
    int t[n], s[n], used[n];
    for (int i = 0; i < n; i++) {
      cin >> s[i];
      used[i] = 0;
    }
    for (int i = 0; i < n; i++) {
      cin >> t[i];
    }
    bool found_i;
    for (int i = 0; i < n; i++) {
      found_i = false;
      for (int j = 0; j < n; j++) {
        if (used[j] == 0 && (abs(s[j] - t[i]) % k == 0 ||
            (t[i] + s[j]) % k == 0)) {
          used[j] = 1;
          found_i = true;
          break;
        }
      }
      if (!found_i) {
        break;
      }
    }
    bool solved = true;
    for (int i = 0; i < n; i++) {
      if (used[i] == 0) {
        solved = false;
        break;
      }
    }
    if (solved) {
      cout << "YES" << "\n";
    } else {
      cout << "NO" << "\n";
    }
  }
  return 0;
}
