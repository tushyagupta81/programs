#include<iostream>
using namespace std;

int main(){
    int a;
    cin>>a;
    if(a%2!=0){
        cout<<"weird";
    }else{
        if(a>=2 && a<=5){
            cout<<"not weird";
        }else if(a>=6 && a<=20){
            cout<<"weird";
        }else{
            cout<<"not weird";
        }
    }
    return 0;
}
