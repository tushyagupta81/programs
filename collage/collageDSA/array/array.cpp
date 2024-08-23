#include <iostream>
using namespace std;

class Arr {
private:
  int a[100];
  int l;
  int ins;

public:
  Arr() {
    l = sizeof(a) / sizeof(a[0]);
    cout << "Enter number of elements to enter: ";
    cin >> ins;
    if (ins > l) {
      ins = l;
      cout << "Max length of array is -> " << l << "\n";
    }
    for (int i = 0; i < ins; i++) {
      cout << i << ": ";
      cin >> a[i];
    }
  }
  void trav() {
    for (int i = 0; i < ins; i++) {
      cout << a[i] << " ";
    }
    cout << endl;
  }
  void insert_at_end(int ele) {
    a[ins] = ele;
    if (ins != l) {
      ins += 1;
    }
  }
  void insert_at_start(int ele) {
    if (ins != l) {
      for (int i = ins - 1; i >= 0; i--) {
        a[i + 1] = a[i];
      }
    } else {
      for (int i = ins - 2; i >= 0; i--) {
        a[i + 1] = a[i];
      }
    }
    a[0] = ele;
    if (ins != l) {
      ins += 1;
    }
  }
  void insert_at(int ele, int ind) {
    if (ind + 1 > ins) {
      a[ins] = ele;
    } else {
      if (ins != l) {
        for (int i = ins - 1; i >= ind; i--) {
          a[i + 1] = a[i];
        }
      } else {
        for (int i = ins - 2; i >= ind; i--) {
          a[i + 1] = a[i];
        }
      }
      a[ind] = ele;
    }
    if (ins != l) {
      ins += 1;
    }
  }
  void delete_at_end() {
    if (ins != 0) {
      a[ins - 1] = 0;
      ins -= 1;
    } else {
      cout << "No elements in array" << endl;
    }
  }
  void delete_at_start() {
    if (ins != 0) {
      for (int i = 0; i < ins - 1; i++) {
        a[i] = a[i + 1];
      }
      a[ins - 1] = 0;
      ins -= 1;
    } else {
      cout << "No elements in array" << endl;
    }
  }
  void delete_at(int ind) {
    if (ins != 0) {
      if (ind + 1 > ins) {
        a[ins - 1] = 0;
      } else {
        for (int i = ind; i < ins - 1; i++) {
          a[i] = a[i + 1];
        }
        a[ins - 1] = 0;
      }
      ins -= 1;
    } else {
      cout << "No elements in array" << endl;
    }
  }
  void search(int term) {
    for (int i = 0; i < ins; i++) {
      if (a[i] == term) {
        cout << term << " at index " << i << "\n";
        return;
      }
    }
    cout << term << " not found" << "\n";
  }
};

int main() {
  Arr yay;
  yay.trav();
  cout << "Inserting 5 at start" << endl;
  yay.insert_at_start(5);
  yay.trav();
  cout << "Inserting 10 at end" << endl;
  yay.insert_at_end(10);
  yay.trav();
  cout << "Inserting 20 at index 3" << endl;
  yay.insert_at(20, 3);
  yay.trav();
  cout << "Deleting element at index 3" << endl;
  yay.delete_at(3);
  yay.trav();
  cout << "Deleting element at start" << endl;
  yay.delete_at_start();
  yay.trav();
  cout << "Deleting element at end" << endl;
  yay.delete_at_end();
  yay.trav();
  cout << "Search for 10" << endl;
  yay.search(10);
  return 0;
}
