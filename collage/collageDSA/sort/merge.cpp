#include <iostream>
using namespace std;

int main() {
  int na, nb;
  cout << "Enter length for array a: ";
  cin >> na;
  int a[na];
  for (int i = 0; i < na; i++) {
    cin >> a[i];
  }
  cout << "Enter length for array b: ";
  cin >> nb;
  int b[nb];
  for (int i = 0; i < nb; i++) {
    cin >> b[i];
  }
  int c[na + nb];
  int i = 0, j = 0, p = 0;
  while (i < na && j < nb) {
    if (a[i] < b[j]) {
      c[p] = a[i];
      p++;
      i++;
    } else {
      c[p] = b[j];
      p++;
      j++;
    }
  }
  if (i >= na) {
    while (j < nb) {
      c[p] = b[j];
      p++;
      j++;
    }
  } else if (j >= nb) {
    while (i < na) {
      c[p] = a[i];
      p++;
      i++;
    }
  }
  for (int i = 0; i < na + nb; i++) {
    cout << c[i] << " ";
  }
  return 0;
}
