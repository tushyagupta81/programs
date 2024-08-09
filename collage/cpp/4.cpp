#include<iostream>
using namespace std;

int main(){
    int a;
    cin>>a;
    long b[a];
    long s = 0;
    for(int i=0;i<a;i++){
        cin>>b[i];
        s+=b[i];
    }
    cout<<s;
}
