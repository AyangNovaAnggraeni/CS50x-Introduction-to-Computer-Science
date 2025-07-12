// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
 *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';

}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO

    // Open the dictionary file
    FILE *source = fopen(dictionary, "r");
    if( source == NULL)
    {
        printf("cpuldn't open\n");
        return false;
    }
    // Read each word in the file

    char word[LENGTH + 1];
    while (fscanf( source, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if ( n == NULL)
        {
            return false;
        }
        strcpy(n->word,word);
        int index= hash(word);
        n->next = table[index];
        table[index] = n;
    }

        // Add each word to the hash table

    // Close the dictionary file
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    int count;
    for ( int i = 0; i < table[N]; i++)
    {
        char word[LENGTH + 1]++;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    free()
    return false;
}
