#include<iostream>
using namespace std;

int main(){
    int a;
    cin>>a;
    int b[a][a];
    int s1 = 0,s2 = 0;
    for(int i=0;i<a;i++){
        for(int j=0;j<a;j++){
            cin>>b[i][j];
            if(i==j){
                s1+=b[i][j];
            }
            if((i+j) == a-1){
                s2+=b[i][j];
            }
        }
    }
    int s = s1-s2;
    if(s<0){
        s = -s;
    }
    cout<<s;
}
