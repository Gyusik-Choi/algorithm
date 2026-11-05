#include <string.h>

int get_max(const int a, const int b) {
    return a >= b ? a : b;
}

int lengthOfLongestSubstring(char* s) {
    int arr[128] = {0};
    int longest = 0;
    int left = 0;
    const int length = (int) strlen(s);
    for (int right = 0; right < length; right++) {
        const char c = s[right];
        while (arr[c] > 0) {
            arr[s[left++]] = 0;
        }
        arr[c] = 1;
        longest = get_max(longest, right - left + 1);
    }
    return longest;
}
