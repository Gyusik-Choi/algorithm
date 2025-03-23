#include <stdio.h>

int main(void) {
    char str[21];  // Input string (max 20 digits + 1 null terminator)
    int nums[20]; // Array to store individual digits
    int length = 0; // Counter for number of digits

    scanf_s("%s", str, (unsigned int)sizeof(str)); // Read input as string

    // Convert each character to an integer
    for (int i = 0; str[i] != '\0'; i++) {
        nums[length] = str[i] - '0';
        length++;
    }

    int max_num = 0;

    for (int i = 0; i < length; i++) {
        if (max_num == 0 || nums[i] == 0 || max_num == 1 || nums[i] == 1) {
            max_num += nums[i];
            continue;
        }
        max_num *= nums[i];
    }

    printf("%d", max_num);
    return 0;
}
