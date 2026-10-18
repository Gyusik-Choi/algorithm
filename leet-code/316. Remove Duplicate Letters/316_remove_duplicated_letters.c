#include <stdlib.h>
#include <string.h>

char* removeDuplicateLetters(char* s) {
    const int size = (int) strlen(s);
    int top = 0;
    char* stack = malloc(size + 1);
    int stack_counter[26] = {0};
    int counter[26] = {0};

    for (int i = 0; i < size; i++) {
        counter[s[i] - 'a']++;
    }
    for (int i = 0; i < size; i++) {
        const char c = s[i];
        counter[c - 'a']--;
        if (stack_counter[c - 'a'] > 0) {
            continue;
        }
        while (top > 0 && stack[top - 1] > c && counter[stack[top - 1] - 'a'] > 0) {
            stack_counter[stack[--top] - 'a']--;
        }
        stack[top++] = c;
        stack_counter[stack[top - 1] - 'a']++;
    }
    // 문자열 배열로 반환하기 위해 마지막 자리에 '\0' 추가
    stack[top] = '\0';
    return stack;
}
