#include <cs50.h>
#include <stdio.h>

int get_positive_height(void);
void print_row(int height, int space);

int main(void)
{
    int height = get_positive_height();
    for (int i = 0; i < height; i++)
    {
        // print row of bricks
        print_row(i + 1, height - i - 1);
    }
}

// handle negative number
int get_positive_height(void)
{
    int height;
    do
    {
        // ask user for the height
        height = get_int("height: ");
    }
    while (height < 1);
    return height;
}

// make a function to display
void print_row(int height, int space)
{
    // print spaces
    for (int i = 0; i < space; i++)
    {
        printf(" ");
    }
    // print bricks
    for (int i = 0; i < height; i++)
    {
        printf("#");
    }
    printf("\n");
}
