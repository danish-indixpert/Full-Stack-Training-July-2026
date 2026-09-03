#include<stdio.h>
int main()
{
int num1[5]={1,2,3,4,5};
int num2[3]={6,7,8};
int num3[8];
int i;

for(int i=0;i<5;i++)
{
    num3[i]=num1[i];
}
for(int i=0;i<3;i++)
{
    num3[i+5]=num2[i];
}
for(int i=0;i<8;i++)
{
    printf("%d ", num3[i]);
}
return 0;
}