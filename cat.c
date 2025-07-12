#include <cs50.h>
#include <stdio.h>

void meow(int n);
int get_positive_times(void);

int main(void)
{
    int n = get_positive_times(); 
    meow(n);
}

int get_positive_times()
{
    int times;
    do
    {
        times = get_int("number : ");
    }
    while (times < 1);
    return times;
}

void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
