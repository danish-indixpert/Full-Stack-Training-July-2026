#include<stdio.h>
int main(){
    int a1[5]={1,2,3,4,5};
    int a2[3]={6,7,8};
    int a3[8];
    int i;

    for(int i=0;i<5;i++)
    {

        printf("%d", a3[i]=a1[i]);
    }
    for(int i=0;i<3;i++)
{
    printf("%d", a3[i+5]=a2[i]);

}
for(int i=0;i<8;i++)
{
printf("%d", a3[i]);
}

return 0;
}


