#include<stdio.h>
#include<string.h>
int c(char[100],char);

int main(){
    int n;
    char ch,s[100];
    gets(s);
    fflush(stdin);
    printf("count for: ");
    scanf("%c",&ch);
    n = c(s,ch);
    printf("%d of %c",n,ch);
    return 0;
}
int c(char s[100],char ch){
    int count = 0,i;
    for(i=0;i<strlen(s);i++){
        if(s[i]==ch){
            count++;
        }
    }
    return count;
}