#include<stdio.h>

int main(){
    int i,a,d,pd;
    scanf("%d",&a);
    pd = a%10;
    for(i=1;i<=3;i++){
        d = a%10;
        if(d>pd){
            printf("Not a well ordered number");
            return 0;
        }
        a = a/10;
        pd = d;
    }
    printf("Well ordered number");
    return 0;
}