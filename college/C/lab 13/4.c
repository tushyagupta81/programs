#include<stdio.h>

int main(){
    FILE *a,*b;
    a = fopen("copy.txt","r");
    b = fopen("write.txt","w");
    char c;
    while((c=getc(a)) != EOF){
        fputc(c,b);
    }
    fclose(a);
    fclose(b);
    return 0;
}