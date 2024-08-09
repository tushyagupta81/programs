#include<stdio.h>
#include<string.h>

int main(){
    char a[100],b[100];
    int i;
    gets(a);
    for(i = (strlen(a)-1);i>=0;i--){
        b[strlen(a)-i] = a[i];
    }
    puts(b);
    return 0;
}