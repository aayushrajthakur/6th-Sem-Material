#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include<stdlib.h>
#include <ctype.h>

// Function to check if the character is a delimiter
bool isDelimiter(char ch) {
    return (ch == ' ' || ch == '+' || ch == '-' || ch == '*' || ch == '/' || 
            ch == ',' || ch == ';' || ch == '>' || ch == '<' || ch == '=' || 
            ch == '(' || ch == ')' || ch == '[' || ch == ']' || ch == '{' || ch == '}');
}

// Function to check if the character is an operator
bool isOperator(char ch) {
    return (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '>' || ch == '<' || ch == '=');
}

// Function to check if the string is a valid identifier
bool isValidIdentifier(char* str) {
    if (isdigit(str[0]) || isDelimiter(str[0])) return false;
    return true;
}

// Function to check if the string is a keyword
bool isKeyword(char* str) {
    char* keywords[] = {"if", "else", "while", "do", "break", "continue", "int", "double", "float", 
                        "return", "char", "case", "sizeof", "long", "short", "typedef", "switch", 
                        "unsigned", "void", "static", "struct", "goto"};
    for (int i = 0; i < 22; ++i) {
        if (strcmp(str, keywords[i]) == 0) return true;
    }
    return false;
}

// Function to check if the string is an integer
bool isInteger(char* str) {
    int len = strlen(str);
    if (len == 0) return false;
    for (int i = 0; i < len; i++) {
        if (!isdigit(str[i])) return false;
    }
    return true;
}

// Function to check if the string is a real number
bool isRealNumber(char* str) {
    int len = strlen(str);
    bool hasDecimal = false;
    if (len == 0) return false;
    for (int i = 0; i < len; i++) {
        if (str[i] == '.') {
            if (hasDecimal) return false;
            hasDecimal = true;
        } else if (!isdigit(str[i])) {
            return false;
        }
    }
    return true;
}

// Function to extract the substring
char* subString(char* str, int left, int right) {
    int i;
    char* subStr = (char*)malloc(sizeof(char) * (right - left + 2));
    for (i = left; i <= right; i++) {
        subStr[i - left] = str[i];
    }
    subStr[right - left + 1] = '\0';
    return subStr;
}

// Function to parse the input string
void parse(char* str) {
    int left = 0, right = 0;
    int len = strlen(str);

    while (right <= len && left <= right) {
        if (!isDelimiter(str[right])) {
            right++;
        }

        if (isDelimiter(str[right]) && left == right) {
            if (isOperator(str[right])) {
                printf("'%c' is an operator\n", str[right]);
            }
            right++;
            left = right;
        } else if (isDelimiter(str[right]) && left != right || (right == len && left != right)) {
            char* subStr = subString(str, left, right - 1);

            if (isKeyword(subStr)) {
                printf("'%s' is a keyword\n", subStr);
            } else if (isInteger(subStr)) {
                printf("'%s' is an integer\n", subStr);
            } else if (isRealNumber(subStr)) {
                printf("'%s' is a real number\n", subStr);
            } else if (isValidIdentifier(subStr) && !isDelimiter(str[right - 1])) {
                printf("'%s' is a valid identifier\n", subStr);
            } else if (!isValidIdentifier(subStr) && !isDelimiter(str[right - 1])) {
                printf("'%s' is not a valid identifier\n", subStr);
            }

            left = right;
        }
    }
}

int main() {
    char str[100] = "int a = b + 1.23; // example input";
    parse(str);
    return 0;
}
