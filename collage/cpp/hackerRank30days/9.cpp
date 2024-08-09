#include<iostream>
using namespace std;

int factorial(int);

int main(){
    int a;
    cin>>a;
    int f=factorial(a);
    cout<<f;
    return 0;
}

int factorial(int t){
    if(t==1){
        return t*1;
    }else{
        return t*factorial(t-1);
    }
}
