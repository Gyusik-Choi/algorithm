#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int to_left[numsSize];
    int to_right[numsSize];
    to_left[0] = nums[0];
    to_right[numsSize - 1] = nums[numsSize - 1];
    for (int i = 1; i < numsSize; i++) {
        to_left[i] = to_left[i - 1] * nums[i];
    }
    for (int i = numsSize - 2; i >= 0; i--) {
        to_right[i] = to_right[i + 1] * nums[i];
    }
    *returnSize = numsSize;
    int* answer = malloc(sizeof(int) * numsSize);
    answer[0] = to_right[1];
    answer[numsSize - 1] = to_left[numsSize - 2];
    for (int i = 1; i < numsSize - 1; i++) {
        answer[i] = to_left[i - 1] * to_right[i + 1];
    }
    return answer;
}