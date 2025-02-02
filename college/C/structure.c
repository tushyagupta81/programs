#include<stdio.h>
#include<string.h>

void main(){
    int i;
    struct student{
        int r;
        char n[10];
        float m;
    };
    struct student *p,S1;
    p = &S1;
    printf("r,n,m\n");
    scanf("%d %s %f",&S1.r,&S1.n,&S1.m);
    int l = 0;
    char str[100];
    strcpy(str,S1.n);
    for(i=0; str[i] != '\0' ;i++){
        l++;
    }
    printf("length = %d\n",l);
    printf("l2 = %d\n",strlen(str));
    printf("%d %s %f",S1.r,S1.n,S1.m);
    printf("%d %s %f",p->r,p->n,p->m);
}