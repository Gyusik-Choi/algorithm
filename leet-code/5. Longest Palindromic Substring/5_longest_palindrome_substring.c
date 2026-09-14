#include <stdlib.h>
#include <string.h>

static void find_palindrome(const char* s, const int s_size, int left, int right, int* left_ref, int* right_ref) {
    while (0 <= left && right < s_size && s[left] == s[right]) {
        left--;
        right++;
    }
    *left_ref = left + 1;
    *right_ref = right - 1;
}

char* longestPalindrome(char* s) {
    int max_left = 0;
    int max_right = 0;
    const int s_length = (int) strlen(s);
    for (int i = 0; i < s_length; i++) {
        int left;
        int right;
        find_palindrome(s, s_length, i, i, &left, &right);
        if (max_right - max_left < right - left) {
            max_left = left;
            max_right = right;
        }
        find_palindrome(s, s_length, i, i + 1, &left, &right);
        if (max_right - max_left < right - left) {
            max_left = left;
            max_right = right;
        }
    }
    const int palindrome_length = max_right - max_left + 1;
    // 문자열 종료 표시를 위한 '\0' 자리를 확보하기 위해 palindrome_length + 1 로 동적 할당
    char* palindrome = malloc(palindrome_length + 1);
    if (palindrome == NULL) {
        return NULL;
    }
    memcpy(palindrome, s + max_left, palindrome_length);
    palindrome[palindrome_length] = '\0';
    return palindrome;
}
