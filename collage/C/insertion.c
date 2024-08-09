#include<stdio.h>

int main(){
    int i,j,a[10],temp;
    for(i=0;i<10;i++){
        scanf("%d",&a[i]);
    }
    for(i=1;i<10;i++){
        temp = a[i];
        j = i-1;
        while(j>=0 && a[j]>temp){
            a[j+1] = a[j];
            j-=1;
        }
        a[j+1] = temp;
    }
    printf("\n\n\n");
    for(i=0;i<10;i++){
        printf("%d\n",a[i]);
    }
    return 0;
}