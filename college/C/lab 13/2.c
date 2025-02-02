#include<stdio.h>

int fib(int,int,int);

int main(){
    int n;
    scanf("%d",&n);
    fib(0,1,n);
    return 0;
}

int fib(int a,int b,int n){
    if(a>n){
        return 0;
    }
    printf("%d ",a);
    fib(b,a+b,n);
}