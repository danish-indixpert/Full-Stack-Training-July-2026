#include<stdio.h>
    int add();
    int subtraction();
    int multiply();
    int division();
        int Add()
            {
                int a=10;
                int b=5;
                printf("\nSum: %d\n", a+b);

            }
        int Subtraction()
            {
                int a=20;
                int b=50;
                printf("Subtraction: %d\n", a-b);

            }
        int Multiply()
            {

                int a=5;
                int b=15;
                printf("Multiply: %d\n", a*b);
            }
        int Division()
            {
                int a=50;
                int b=6;
                printf("Division: %d\n", a/b);

            }

int main()
{
printf("\nOutput |\n");

    Add();
    Subtraction();
    Multiply();
    Division();

return 0;
}