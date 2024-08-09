#include<stdio.h>
#include<string.h>

void count(char[100]);

int main(){
    char s[100];
    gets(s);
    count(s);
    return 0;
}

void count(char s[100]){
    int v=0,c=0,b=0,d=0;
    int i,j;
    char vc[10]= {'a','e','i','o','u','A','E','I','O','U'};
    for(i=0;i<(strlen(s));i++){
        if((s[i]>=97&&s[i]<=122)||(s[i]>=65&&s[i]<=90)){
            for(j=0;j<10;j++){
                if(s[i]==vc[j]){
                    v++;
                    goto m_label;
                }
            }
            c++;
            m_label:
        }else if(s[i] == ' '){
            b++;
        }else if(s[i]>=48&&s[i]<=57){
            d++;
        }
    }
    printf("v=%d, c=%d, b=%d, d=%d",v,c,b,d);
}