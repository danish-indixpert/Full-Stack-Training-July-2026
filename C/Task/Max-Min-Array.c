#include<stdio.h>
int main()
{
    int num[10]={2,4,1,8,56,5,78,11,9,6};
    int maximum=num[0];
    int minimum=num[0];
    int i;

        for(int i=0;i<10;i++)
        {
            if(num[i]>maximum)
        {

            maximum=num[i];
        }

            if(num[i]<minimum)
        {
            minimum=num[i];
        }
    }

    printf("\n=== Output Number ===\n");

    printf("maximum number:%d\n", maximum);
    printf("minimum number:%d", minimum);

return 0;
}