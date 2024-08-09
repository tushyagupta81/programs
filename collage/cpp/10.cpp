#include<iostream>
using namespace std;

int main(){
    int a;
    cin>>a;
    long b=0,m=1;
    while(a!=0){
        b = b + (a%2)*m;
        a = a/2;
        m = m*10;
        // cout<<b<<endl;
    }
    // cout<<"final"<<b<<endl;
    int max=0;
    int t=0;
    while(b!=0){
        if(b%10==1){
            t++;
        }else{
            t=0;
        }
        if(t>max){
            max=t;
        }
        // cout<<b<<endl;
        b=b/10;
    }
    cout<<max;
    return 0;
}
