#include<cmath>
#include<iostream>
using namespace std;

int main(){
    double a;
    int b,c;
    cin>>a>>b>>c;
    double f;
    f = a + (a*(b+c))/100;
    cout<<round(f);
    return 0;
}
