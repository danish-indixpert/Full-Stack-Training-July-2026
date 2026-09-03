#include<stdio.h>
void menu();
void A_player_id(int player_id);
void B_name(char name[]);
void C_country_name(char country_name[]);
void menu()
{
printf("\n1. Player ID");
printf("\n2. Name");
printf("\n3. Country Name");
printf("\n4. Exit");
}

int main()
{

    int player_id;
    char name[50]; 
    char country_name[50];
    int option;

    while(1)
    {

        menu();
        printf("\nPlease Select Any Option: ");
        scanf("%d", &option);

        if(option==4)
        {
            printf("Exit\n");
            break;
        }
        printf("\nPlease Enter Player ID: ");
        scanf("%d", &player_id);


        printf("\nPlease Enter Name: ");
        scanf("%s", &name);

        printf("\nPlease Enter Country Name: ");
        scanf("%s", &country_name);
    

        switch (option)
        {
        case 1:
                A_player_id(player_id);
                break;

            case 2:
                B_name(name);
                break;

            case 3:
                C_country_name(country_name);
                break;

        default:
        printf("Please Enter Valid Option");
            break;
        }
    }

return 0;
}


void A_player_id(int player_id)
{
    printf("Player ID: %d\n", player_id);
}

void B_name(char name[])
{
    printf("Name: %s\n", name);
}

void C_country_name(char country_name[])
{
    printf("Country Name: %s\n", country_name);
}