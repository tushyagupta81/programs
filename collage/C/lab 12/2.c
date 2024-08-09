#include<stdio.h>
struct stu{
    char student_name[100];
    int roll_no;
    float marks;
} s[2];
int main(){
    int i;
    for(i=0;i<2;i++){
        fflush(stdin);
        printf("Enter name: ");
        gets(s[i].student_name);
        printf("Enter roll no: ");
        scanf("%d",&s[i].roll_no);
        printf("Enter marks: ");
        scanf("%f",&s[i].marks);
    }
    for(i=0;i<2;i++){
        printf("\nName: %s\n",s[i].student_name);
        printf("Roll no: %d\n",s[i].roll_no);
        printf("Marks: %f\n",s[i].marks);
    }
    return 0;
}