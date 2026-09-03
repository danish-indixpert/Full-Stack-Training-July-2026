#include<stdio.h>
#include<string.h>
int main()
{
    int choice;
    int option;
    int seats;
    int cancel;
    int check_bus;
    char reg_username[50];
    char reg_password[50];
    char reg_email[30];
    char log_password[50];
    char log_email[30];
    char passenger_name[20];
    int payment_method;
    int bus_no;
    char sourcecity[50];
    char destinationcity[50];
    int total_seats=50;
    int available_seats=50;
    int ticketprice=500;
    int id;
    int age;

    printf("\n********** Bus Reservation System **********\n");
    printf("\n==========================================");
    printf("\n*              Registration              *");
    printf("\n==========================================");

    printf("\n1. Registration");
    printf("\n2. Exit");

    printf("\nPlease Enter Your Option: ");
    scanf("%d", &option);


    if(option == 2)
        {
            printf("\nRegistration Exit. Thank You!");

        }
            else
        {

    printf("Please Enter Full Name: ");
    scanf(" %[^\n]", reg_username);

    printf("Please Enter Email ID: ");
    scanf("%s", reg_email);

    printf("Please Enter Your Password: ");
    scanf("%s", reg_password);

    printf("Please Enter ID: ");
    scanf("%d", &id);

    printf("Please Enter Age: ");
    scanf("%d", &age);

    printf("\n\n-----      Registration Successful!       -----\n");

    printf("Username:       %s\n", reg_username);
    printf("Email ID:       %s\n", reg_email);
    printf("Password:       %s\n", reg_password);
    printf("ID:             %d\n", id);
    printf("Age:            %d\n", age);

    printf("\n==========================================");
    printf("\n*                 Login                  *");
    printf("\n==========================================");

        {
            printf("\n1. Login");
            printf("\n2. Exit");
        }

        printf("\nPlease Enter Your Choice: ");
        scanf("%d", &choice);
   
        if(choice==2)
        {
            printf("\nLogin Exit. Goodbye!");
        }
        else
        {
    
        printf("Please Enter Email ID: ");
        scanf("%s", log_email);

        printf("Please Enter Password: ");
        scanf("%s", log_password);

        if(strcmp(reg_email,log_email)==0 &&
            strcmp(log_password,reg_password)==0)
           
        {

            printf("\nLogin Successful. Welcome, ! %s\n ", reg_username);
        }

        else

        {
            printf("\ninvalid username or password");
            return 0;

        }
    do
    {
        /* code */

        printf("\n********** USER MENU **********\n");
        printf("1. Book a Ticket\n");
        printf("2. Cancel a Ticket\n");
        printf("3. Check Bus Status\n");
        printf("4. Logout\n");

        printf("Enter Your Choice: ");
        scanf("%d", &choice);

    switch (choice)
    {
        case 1:
        {

        printf("Enter Passenger Name: ");
        scanf(" %[^\n]", passenger_name);

        printf("Enter Bus Number: ");
        scanf("%d", &bus_no);

        printf("Enter Source City: ");
        scanf("%s", sourcecity);

        printf("Enter Destination City: ");
        scanf("%s", destinationcity);

        printf("Enter Number Of Seats: ");
        scanf("%d", &seats);

            printf("Payment Method: ");
            
            printf("\n1. UPI");
            printf("\n2. Debit Card");
            printf("\n3. Credit Card");

            printf("\nPlease Enter Payment Option: ");
            scanf("%d", &payment_method);

            printf("\nPayment Successful!\n");

                if(seats<=available_seats)
                {
                available_seats=available_seats-seats;
                printf("\n       *Ticket Booked*         \n");
                printf("Passenger Name:     %s\n", passenger_name);
                printf("Source City:        %s\n", sourcecity);
                printf("Destination City:   %s\n", destinationcity);
                printf("Bus Number:         %d\n", bus_no);
                printf("Seats Booked:       %d\n", seats);
                printf("Total Price:        %d\n", seats*ticketprice);
                printf("Payment Method:     %d\n", payment_method);
                }
                else
                {
                printf("\nSeats Not available!");
                }
                break;
                }

        case 2:
        {

            printf("Enter Bus Number: ");
            scanf("%d", &bus_no);

            printf("\nEnter Number Of Seats to Cancel: ");
            scanf("%d", &cancel);

                available_seats=available_seats+cancel;
                if(available_seats>total_seats)

                {
                available_seats=total_seats;

                }

                printf("\nCancellation Successful! %d seats canceled on Bus Number %d\n", cancel,bus_no);
                break;
                }

        case 3:
        {

            printf("Please Enter Bus Number: ");
            scanf("%d", &check_bus);

            if(check_bus==bus_no)
                {
                    printf("Bus Number:         %d\n", bus_no);
                    printf("Source City:        %s\n", sourcecity);
                    printf("Destination City:   %s\n", destinationcity);
                    printf("Total Seats:        %d\n", total_seats);
                    printf("Available Seats:    %d\n", available_seats);
                    printf("Ticket Price:       %d\n", ticketprice);
                }
                else
                {
                printf("\n=====- Bus Not Found! -=====\n");
                }
            break;
            }
        case 4:
        {
            printf("\nLogout Successful!");
            break;
        } 
            default:
            {
                printf("Invalid Choice");
                break;
            }
        }
} while (choice !=4);

    }
}
return 0;
}