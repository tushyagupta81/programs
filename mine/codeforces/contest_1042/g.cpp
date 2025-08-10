#include <functional>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
  int test_cases;
  cin >> test_cases;
  for (int test_case = 0; test_case < test_cases; test_case++) {
    int n, k;
    cin >> n;
    cin >> k;
    priority_queue<int, vector<int>, greater<int>> s;
    int t;
    for (int i = 0; i < n; i++) {
      cin >> t;
      s.push(t);
    }
    long score = 1;

    int min_val;
    for (int i = 0; i < k; i++) {
      min_val = s.top();
      s.pop();
      score = ((long) score * min_val) % 1000000007;
      // cout << score << "\n";
      for (int j = 1; j < min_val; j++) {
        s.push(j);
      }
    }

    cout << score % 1000000007 << "\n";
  }
  return 0;
}
