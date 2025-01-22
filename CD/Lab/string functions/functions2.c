#include<stdio.h>
#include<string.h>
void main() {
    char word1[] = "Hello ";
    char word2[] = "Hello ";
    char word3[] = "World ";
    char word4[20];

    printf("The concatenated word is : %s ",strcat(word1, word2));
    printf("\nThe comparing between word1 and word2 is : %d.",strcmp(word1, word2));
    printf("\nThe comparing between word1 and word3 is : %d.",strcmp(word1, word3));
    //printf("\nThe comparing between word1 and word3 is : %d.",strcmp(word1, word3));
    strcpy(word4, word1); //It copy the value of word1 in word4.
    printf("\nThe value of word1 is copied in word4 : %s.",word4);
}