#include<stdio.h>
#include<string.h>
char username[50] = "admin", password[15] = "12345";

int main(){
    char urname[50], pswd[15];
    
    int cond = 1;
    do {
        printf("Enter the username(upto 50 characters): ");
        scanf("%s",urname);
        printf("Enter the password(upto 15 characters) : ");
        scanf("%s",pswd);
        if((strcmp(username,urname)== 0) && (strcmp(password,pswd) == 0)){
            printf("Access Granted, welcome to the panel..!!");
            cond = 0;
        }
        else if((strcmp(username,urname) != 0) && (strcmp(password,pswd) == 0)){
            printf("Invalid Username..,Try again.!!");
        }
        else if((strcmp(username,urname) == 0) && (strcmp(password,pswd) != 0)){
            printf("Invalid password, Try again..!!");
        }
    } while(cond);
    
}