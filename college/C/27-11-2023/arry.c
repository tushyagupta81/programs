#include<stdio.h>

int main(){
    int a[100],s=0,i,j,n,smal,lar;
    float m;
    printf("Number of elemets in array: ");
    scanf("%d",&n);
    printf("Array -> \n");
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    lar = a[0];
    smal = a[0];
    for(i=0;i<n;i++){
        s+= a[i];
        if(a[i]>lar){
            lar = a[i];
        }
        if(a[i]<smal){
            smal = a[i];
        }
    }
    m =(float) s/n;
    printf("Sum = %d, mean = %f, largest = %d, smallest = %d\n",s,m,lar,smal);
    for(i=(n-1);i>=0;i--){
        printf("%d ",a[i]);
    }
    return 0;
}