#include <cs50.h>
#include <stdio.h>

int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    int quarters = calculate_quarters(cents);
    cents = cents - (quarters * 25);

    int dimes = calculate_dimes(cents);
    cents = cents - (dimes * 10);

    int nickels = calculate_nickels(cents);
    cents = cents - (nickels * 5);

    int pennies = calculate_pennies(cents);
    cents = cents - (pennies * 1);

    printf("%i\n", quarters + dimes + nickels + pennies);
}

int calculate_quarters(int cents)
{
    int quarters;
    for (quarters = 0; cents >= 25; quarters++)
    {
        cents -= 25;
    }
    return quarters;
}

int calculate_dimes(int cents)
{
    int dimes;
    for (dimes = 0; cents >= 10; dimes++)
    {
        cents -= 10;
    }
    return dimes;
}

int calculate_nickels(int cents)
{
    int nickels;
    for (nickels = 0; cents >= 5; nickels++)
    {
        cents -= 5;
    }
    return nickels;
}

int calculate_pennies(int cents)
{
    int pennies;
    for (pennies = 0; cents >= 1; pennies++)
    {
        cents -= 1;
    }
    return pennies;
}
