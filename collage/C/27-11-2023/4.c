#include<stdio.h>

int main(){
    int a[100][100],b[100][100],c[100][100],d[100][100],i,j,m,n;
    printf("Enter dimension of matrix: ");
    scanf("%d %d",&m,&n);
    printf("A:\n");
    for(i=0;i<m;i++){
        for(j=0;j<n;j++){
            scanf("%d",&a[i][j]);
        }
    }
    printf("B:\n");
    for(i=0;i<m;i++){
        for(j=0;j<n;j++){
            scanf("%d",&b[i][j]);
        }
    }
    for(i=0;i<m;i++){
        for(j=0;j<n;j++){
            c[i][j] = a[i][j] + b[i][j];
        }
    }
    for(i=0;i<m;i++){
        for(j=0;j<n;j++){
            d[i][j] = a[i][j] - b[i][j];
        }
    }
    printf("Addition of matix: \n");
    for(i=0;i<m;i++){
        for(j=0;j<n;j++){
            printf("%d ",c[i][j]);
        }
        printf("\n");
    }
    printf("Subtraction of matix: \n");
    for(i=0;i<m;i++){
        for(j=0;j<n;j++){
            printf("%d ",d[i][j]);
        }
        printf("\n");
    }
    return 0;
}