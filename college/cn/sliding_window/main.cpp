#include <cstdlib>
#include <ctime>
#include <iostream>
using namespace std;

void send(int i, int *sent, int *rec) {
  sent[i] = 1;
  rec[i] = 1;
}

int main() {
  srand(time(NULL));
  int window_size, window_pos = 0, n_frames = rand() % 95 + 5;
  int sent[n_frames];
  int recived[n_frames];
  for (int i = 0; i < n_frames; i++) {
    sent[i] = 0;
    recived[i] = 0;
  }
  cout << "Frames = " << n_frames << "\n";
  cout << "Enter window size: ";
  cin >> window_size;
  int i;
  bool f;
  while (1) {
    i = window_pos;
    while (i < window_pos + window_size) {
      if (sent[i] == 0) {
        cout << "Sending " << i << "\n";
        send(i, sent, recived);
      }
      i++;
    }
    cout<<"\n";
    i = window_pos;
    while (i < window_size + window_pos) {
      if (recived[i] == 1) {
        cout << "Recived " << i << "\n";
        cout << "Window moved\n";
        window_pos++;
        i++;
      } else {
        break;
      }
    }
    cout<<"\n";
    f = true;
    for (int j = 0; j < n_frames; j++) {
      if (recived[j] == 0) {
        f = false;
        break;
      }
    }
    if (f) {
      cout << "Done all\n";
      break;
    }
  }
  return 0;
}
