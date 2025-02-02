#include<iostream>
using namespace std;

int main() {
    int a;
    cin>>a;
    int b[a];
    int c[a];
    for(int i=0;i<a;i++){
        cin>>b[i];
        c[a-i-1] = b[i];
    }
    for(int i=0;i<a;i++){
        cout<<c[i];
        if(i!=a-1){
            cout<<" ";
        }
    }
    return 0;
}
