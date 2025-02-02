#include<stdio.h>

union u{
    int a;
    char b;
    float c;
}u1;

struct s{
    int d;
    char e;
    float f;
}s1;

int main(){
    printf("For structure: \n");
    printf("int: ");
    scanf("%d",&s1.d);
    printf("char: ");
    fflush(stdin);
    scanf("%c",&s1.e);
    printf("float: ");
    scanf("%f",&s1.f);
    printf("int = %d, char = %c, float = %f\n",s1.d,s1.e,s1.f);
    printf("For union: \n");
    printf("int: ");
    scanf("%d",&u1.a);
    printf("int saved: %d\n",u1.a);
    printf("char: ");
    fflush(stdin);
    scanf("%c",&u1.b);
    printf("char saved: %c\n",u1.b);
    printf("float: ");
    scanf("%f",&u1.c);
    printf("float saved: %f\n",u1.c);
    printf("int = %d, char = %c, float = %f",u1.a,u1.b,u1.c);
    return 0;
}