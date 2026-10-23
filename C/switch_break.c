#include <stdio.h>

int main(void)
{
    float num1, num2; 
    int sign;
    puts("Enter 1st numbers : ");
    scanf("%f", &num1);
    puts("Enter 2st numbers : ");
    scanf("%f", &num2);
    puts("Press\n 1-Addition\n 2-Subtraction\n 3-Multiplication\n 4-Divide");
    scanf("%d", &sign);
    switch(sign)
    {
        case 1 : printf("%.2f + %.2f = %.2f\n", num1, num2, num1 + num2); break;
        case 2 : printf("%.2f - %.2f = %.2f\n", num1, num2, num1 - num2); break;
        case 3 : printf("%.2f * %.2f = %.2f\n", num1, num2, num1 * num2); break;
        case 4 : if(num2 != 0)
                           printf("%.2f / %.2f = %.2f\n", num1, num2, num1 / num2);
                       else
                           puts("Divisor can't be zero");
                 break;
        default : puts("Invalid");
    }
   return 0;
}