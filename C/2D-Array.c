#include <stdio.h>
int main() {
    int marks[5];
    int i; 
    int total = 0;
    char subjects[5][20] = {"sub1", "sub2", "sub3", "sub4", "sub5"};
    float percentage;

    printf("Enter marks:\n");

    for(i = 0; i < 5; i++) 
    {
        printf("%s: ", subjects[i]);
        scanf("%d", &marks[i]);
        total += marks[i];
    }

    percentage = total / 5.0;

    printf("\n--- REPORT ---\n");
    for(i = 0; i < 5; i++) 
    {
        printf("%s = %d\n", subjects[i], marks[i]);
    }

    printf("Total = %d\n", total);
    printf("Percentage = %.2f%%\n", percentage);

    return 0;
}