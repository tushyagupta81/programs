#include<stdio.h>

int main(){
    int a[100],b[100],n,i,j,c,k=0;
    printf("n: ");
    scanf("%d",&n);
    printf("arr:\n");
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++){
        c=0;
        for(j=0;j<n;j++){
            if(a[i]==b[j]){
                c++;
                break;
            }
        }
        if(c==0){
            b[k++] = a[i];
        }
    }
    for(i=0;i<k;i++){
        printf("%d ",b[i]);
    }
    return 0;
}