#include <iostream>
using namespace std;

int main() {
  int test_cases;
  cin >> test_cases;
  for (int k = 0; k < test_cases; k++) {
    int n;
    cin >> n;
    int a[n], b[n];
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
      cin >> b[i];
    }

    int iter = 0;
    bool do_iter = true;
    while (do_iter) {
      do_iter = false;
      // step 1
      for (int j = 0; j < n; j++) {
        if (a[j] > b[j]) {
          do_iter = true;
          a[j] -= 1;
          break;
        }
      }
      // step 2
      for (int j = 0; j < n; j++) {
        if (a[j] < b[j]) {
          a[j] += 1;
          break;
        }
      }
      iter += 1;
    }
    cout << iter << "\n";
  }
}
