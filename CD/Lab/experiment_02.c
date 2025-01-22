#include<stdio.h>
#include<string.h>
#include<ctype.h>
void main() {
    char input[50] = "I have 2 mangoes.";
    printf("%s",input);
    int vowel = 0;
    int cons = 0;
    int dig = 0;
    int spe = 0;

    for(int i=0;i<strlen(input);i++) {
        if(input[i] == 'A' || input[i]=='E' || input[i]=='I' || input[i]=='O' || input[i]=='U' || input[i]=='a' || input[i]=='e' || input[i]=='i' || input[i]=='o' || input[i]=='u'){
            printf("\n%c in %d th space, is a Vowel Letter.",input[i],i+1);
            vowel++;
        }
        else if(isalpha(input[i])){
            printf("\n%c in %d th space, is a consonant Letter.",input[i],i+1);
            cons++;
        }
        else if(isdigit(input[i])) {
            printf("\n%c in %d th space, is a digit.",input[i],i+1);
            dig++;
        }
        else if((int)input[i] >= 33 && (int)input[i] <= 63) {
            printf("\n%c in %d th space, is a special character.",input[i],i+1);
            spe++;
        }
    }
    printf("\n\nTotal no. of Vowels are : %d",vowel);
    printf("\nTotal no. of consonant are : %d",cons);
    printf("\nTotal no. of digits are : %d",dig);
    printf("\nTotal no. of special character are : %d",spe);
}
