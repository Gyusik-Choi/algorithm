#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool isValid(char* s) {
    const int n = (int) strlen(s);
    if (n % 2 != 0) {
        return false;
    }

    char* stack = malloc(n);
    if (stack == NULL) {
        return false;
    }
    int top = 0;

    for (int i = 0; i < n; i++) {
        const char c = s[i];
        if (c == '(' || c == '{' || c == '[') {
            stack[top++] = c;
        } else {
            if (top == 0) {
                free(stack);
                return false;
            }
            const char last = stack[top - 1];
            if ((last == '(' && c != ')') ||
                (last == '{' && c != '}') ||
                (last == '[' && c != ']')) {
                free(stack);
                return false;
            }
            top--;
        }
    }

    const bool result = top == 0;
    free(stack);
    return result;
}
