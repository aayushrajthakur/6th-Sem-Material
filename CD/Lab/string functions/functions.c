#include<stdio.h>
#include<string.h>
void main() {
    char word[] = "Hello World";

    printf("The size of character using strlen : %d ",strlen(word));

    int length = sizeof(word)/sizeof(word[0]);
    printf("\nThe size of character using sizeof : %d ",length);
}