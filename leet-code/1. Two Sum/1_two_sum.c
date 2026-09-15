#include <stdlib.h>

static int compare(const void* a, const void* b) {
    const int* x = *(const int* const*)a;
    const int* y = *(const int* const*)b;
    return (x[0] > y[0]) - (x[0] < y[0]);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int** sorted_nums_with_index = malloc(sizeof(int*) * numsSize);
    for (int i = 0; i < numsSize; i++) {
        sorted_nums_with_index[i] = malloc(sizeof(int) * 2);
        sorted_nums_with_index[i][0] = nums[i];
        sorted_nums_with_index[i][1] = i;
    }

    qsort(sorted_nums_with_index, numsSize, sizeof(int*), compare);

    int* answer = malloc(sizeof(int) * 2);
    *returnSize = 0;
    int left = 0, right = numsSize - 1;
    while (left < right) {
        const int sum = sorted_nums_with_index[left][0] + sorted_nums_with_index[right][0];
        if (sum == target) {
            answer[0] = sorted_nums_with_index[left][1];
            answer[1] = sorted_nums_with_index[right][1];
            *returnSize = 2;
            break;
        }
        if (sum > target) {
            right--;
        } else {
            left++;
        }
    }
    for (int i = 0; i < numsSize; i++) {
        free(sorted_nums_with_index[i]);
    }
    free(sorted_nums_with_index);
    return answer;
}
