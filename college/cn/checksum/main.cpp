#include <bitset>
#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;

int int_to_bin(int a) {
  int temp = 0, m = 1;
  while (a > 0) {
    temp += (a % 10) * m;
    m *= 2;
    a = a / 10;
  }
  return temp;
}

string create_binary_no(int a) {
  string bina = bitset<32>(a).to_string();
  int cut = 0;
  for (int i = 0; i < bina.size(); i++) {
    if (bina[i] == '0') {
      cut = i;
    } else {
      break;
    }
  }
  bina = bina.substr(cut + 1, bina.size() - cut);
  return bina;
}

int binary_division(string bina, int polynomial, int l) {
  int i = 0;
  int bin = int_to_bin(stoi(bina.substr(i, l)));
  i += l;
  while (i < bina.size()) {
    bin = bin ^ polynomial;
    if (bitset<5>(bin).to_string()[0] == '1') {
      // i++;
    } else {
      bin = bin << 1;
      bin += bina[i] == '1' ? 1 : 0;
      i++;
    }
  }
  return bin;
}

int string_to_binary(string a) {
  int bin = 0;
  int m = 1;
  for (int i = a.size() - 1; i >= 0; i--) {
    if (a[i] == '1') {
      bin += m;
    }
    m *= 2;
  }
  return bin;
}

int main() {
  // int polynomial = 0b11001;
  // int l = 5;
  string poly_string;
  cout << "Enter generating polynomial: ";
  cin >> poly_string;
  int l = poly_string.size();
  int polynomial = string_to_binary(poly_string);
  int a;
  cout << "Enter a number: ";
  cin >> a;

  string bina = create_binary_no(a << 4);
  int bin = binary_division(bina, polynomial, l);

  string a_str = create_binary_no(a);
  string final = a_str + bitset<4>(bin).to_string();
  cout << "Final number after Checksum of 4 length checksum: " << final << "\n";

  cout << (binary_division(final, polynomial, l) == 0 ? "Checksum verified"
                                                      : "Checksum failed")<<endl;

  return 0;
}
