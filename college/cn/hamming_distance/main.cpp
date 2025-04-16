#include <iostream>
using namespace std;

int main() {
  int send, rec;
  cout << "Enter send number: ";
  cin >> send;
  cout << "Enter recived number: ";
  cin >> rec;

  int x = send ^ rec;
  int dis = 0;

  while (x > 0) {
    dis += x % 2;
    x = x / 2;
  }
  cout << "Hamming distance: " << dis;
  return 0;
}
