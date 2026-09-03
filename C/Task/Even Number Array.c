#include<stdio.h>
int main()
{
    int num[10]={1,2,3,4,5,6,7,8,9,10};
    int number[10];
    int i;
    int count=0;

for(int i=0;i<10;i++)
{
if(num[i]%2==0)
{

number[count]=num[i];
count++;

}

}

for(int i=0;i<count;i++)

{

    printf("%d ", number[i]);
}

    return 0;
}