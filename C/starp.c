#include <stdio.h>

int main(void)
{
    int i, j, n;
    do //for keep getting input until the conditions met
    {
        printf("Enter Number : ");
        scanf("%d",&n);
    }
    while (n < 1 || n > 8);
    for (i = 1; i <= n; i++) //for each column
    {
        for (j = 1; j <= n; j++) //for each row
        {
            if (j <= n - i)
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        printf("\n");
    }
}
