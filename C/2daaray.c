#include<stdio.h>
int main()
{
char student_name[3][20];
char subject_name[4][10];
int marks[3][3];
int i,j,k;

printf("student details");

for(int i=0;i<3;i++)
{
    for(int i=0;i<20;i++)

{
printf("%s",student_name[i]);
scanf(" %[^\n]", &student_name[i]);


}
}

printf("please enter the sunject name");

  for(int j=0;j<4;j++)

{
    for(int j=0;j<4;j++)


{
printf("%s",subject_name[j]);
scanf("%[^\n]",&subject_name[j]);
}
}

printf("please enter the marks");
for(int k=0;k<3;k++)
{
    for(int k=0;k<3;k++)
{

    printf("%d",marks[k]);
    scanf("%[^\n]",&marks[k]);
}
}
printf("\n");

return 0;

}