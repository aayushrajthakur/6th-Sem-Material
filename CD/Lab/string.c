#include<stdio.h>
#include<string.h>
void main() {
    char letter[1000];
    int i = 0;

    printf("Enter the letter : \n");
    scanf("%s", letter);
    while (letter[i]){
        printf("%c ---> %d\n", letter[i], (int)letter[i]);
        i++;
    }
    
}