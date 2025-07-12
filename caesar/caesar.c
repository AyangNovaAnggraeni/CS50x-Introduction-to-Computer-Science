#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string s);
char rotate(char c, int n);

int main(int argc, string argv[])
{
    // prompting commad line
    if (argc != 2 || !only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    // prompt the user to input the plaintext
    string plaintext = get_string("plaintext: ");

    // convert command line argument from string to int
    int n = atoi(argv[1]);
    // calling the rotate function
    for (int i = 0; i < strlen(plaintext); i++)
    {
        plaintext[i] = rotate(plaintext[i], n);
    }
    printf("ciphertext: %s\n", plaintext);
    return 0;
}

bool only_digits(string s)
{
    int len = strlen(s);
    for (int i = 0; i < len; i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}

char rotate(char c, int n)
{
    if (isupper(c))
    {
        return ((c - 'A' + n) % 26) + 'A';
    }
    else if (islower(c))
    {
        return ((c - 'a' + n) % 26) + 'a';
    }
    return c;
}
