#include<stdio.h>

int fact(int);

int main(){
    int n,r;
    scanf("%d",&n);
    r = fact(n);
    printf("fact = %d",r);
    return 0;
}

int fact(int n){
    if(n==1){
        return 1;
    }else{
        return n * fact(n-1);
    }
}