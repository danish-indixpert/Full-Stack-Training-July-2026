#include<stdio.h>
int main()
{
    int student_id;
    int age;
    char student_name[20];
    char email[30];
    char address[50];

printf("\n===+=== +ENTER STUDENT DETAILS+ ===+===\n");

   
            printf("Please Enter Student_Name :");
            scanf("%s", &student_name);

            printf("Please Enter Age :");
            scanf("%d", &age);
   
            printf("Please Enter Student_ID :");
            scanf("%d", &student_id);

            printf("Please Enter Email :");
            scanf("%s", &email);

            printf("Please Enter Address :");
            scanf("%s", &address);


printf("\n*** STUDENT REPORT ***\n");

            printf("Student_ID   | = %d\n", student_id);    
            printf("Student_Name | = %s\n", student_name);        
            printf("Age          | = %d\n", age);      
            printf("Email        | = %s\n", email);
            printf("Address      | = %s\n", address);                                                                                               
  
    return 0;
}