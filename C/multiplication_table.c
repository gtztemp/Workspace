#include <stdio.h>

int main()
{
    int a, i;
    printf("enter a number-");
    scanf("%d", &a);
    for (i = 1; i < 11; i++)
    {
        printf("%d\n", a * i);
    }
    return 0;
}
