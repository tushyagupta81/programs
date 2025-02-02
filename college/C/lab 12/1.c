#include<stdio.h>
struct ima{
    int real;
    int imaginary;
} s1,s2;

ima sum(ima, ima);

int main(){
    ima r;
    printf("Real and imaginary part(1): ");
    scanf("%d %d",s1.real,s1.imaginary);
    printf("Real and imaginary part(2): ");
    scanf("%d %d",s2.real,s2.imaginary);
    r = sum(s1,s2);
    printf("Sum = %d + %di",r.real,r.imaginary);
    return 0;
}
ima sum(ima a,ima b){
    ima c;
    c.real = a.real + b.real;
    c.imaginary = a.imaginary + b.imaginary;
    return c;
}