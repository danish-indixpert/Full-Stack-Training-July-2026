#include<stdio.h>
int main()
{
int matrix[4][5];
printf("Please Enter The 20 Number \n");
for(int i=0;i<4;i++)
{
    for(int x=0;x<5;x++)
    {
        scanf("%d",&matrix[i][x]);
    }
}
printf("Output |\n");
    for(int i=0;i<4;i++)
{
    for(int x=0;x<5;x++)
    {
        printf("%d ",matrix[i][x]);
    }
    printf("\n");
}
    return 0;
}