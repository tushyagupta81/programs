#include<stdio.h>

void isort(int *,int);

int main(){
    int a[100],b[100];
    int *p;
    p = a;
    int i,n;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    isort(p,n);
    printf("sorted array -> ");
    for(i=0;i<n;i++){
        printf("%d ",a[i]);
    }
    return 0;
}

void isort(int *p,int n){
    int i,j,temp;
    for(i=1;i<n;i++){
        temp = *(p+i);
        j = i-1;
        while(j>=0 && temp<*(p+j)){
            *(p+j+1) = *(p+j);
            j--;
        }
        *(p+j+1) = temp;
    }
}