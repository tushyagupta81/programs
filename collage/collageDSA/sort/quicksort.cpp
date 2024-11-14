#include <iostream>
#include <vector>
using namespace std;

int partition(int (&a)[], int l, int h) {
  int pivot = a[l];
  int j = h, i = l + 1;
  while (j >= i) {
    while (a[j] > pivot && j > l) {
      j--;
    }
    while (a[i] < pivot && i <= h) {
      i++;
    }
    if (i >= j) {
      break;
    }
    swap(a[i], a[j]);
  }
  swap(a[l], a[i - 1]);
  return i - 1;
}

void quicksort(int (&a)[], int l, int h) {
  if (l < h) {
    int p = partition(a, l, h);
    quicksort(a, l, p - 1);
    quicksort(a, p + 1, h);
  }
}

int main() {
  int n;
  cout << "Enter length of array: ";
  cin >> n;
  int a[n];
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }

  quicksort(a, 0, n - 1);

  for (int i = 0; i < n; i++) {
    cout << a[i] << " ";
  }
  return 0;
}
