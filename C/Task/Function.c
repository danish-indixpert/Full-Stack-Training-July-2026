#include<stdio.h>
int add();
int subtraction();
//int division();
int multiply();

int add()
{
    int a = 1, b = 2;
    printf("\nSum| %d\n",a+b);
}


int subtraction()
{
    int a = 1, b = 2;
    printf("Subtraction| %d\n", a-b);
}


//int division()
//{

    //int a = 1, b = 2;
    //printf("Division| %d\n", a/b);
//}



int multiply()

{

    int a = 1, b = 2;
    printf("Multiply| %d\n", 1*2);


}


int main()

{


printf("\nOutput:\n");
    add();
    subtraction();
    //division();
    multiply();


return 0;

}