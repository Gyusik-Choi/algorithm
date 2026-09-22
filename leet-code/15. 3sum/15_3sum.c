#include <stdlib.h>

static int compare(const void* a, const void* b) {
    const int x = *(const int*) a;
    const int y = *(const int*) b;
    return (x > y) - (x < y);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int capacity = 16;
    int** answer = malloc(sizeof(int*) * capacity);
    int idx = 0;
    qsort(nums, numsSize, sizeof(int), compare);
    for (int i = 0; i < numsSize - 2; i++) {
        if (nums[i] > 0) {
            break;
        }
        if (i > 0 && nums[i - 1] == nums[i]) {
            continue;
        }
        int left = i + 1, right = numsSize - 1;
        const int target = -(nums[i]);
        while (left < right) {
            while (left < right && left > i + 1 && nums[left - 1] == nums[left]) {
                left++;
            }
            while (left < right && right < numsSize - 1 && nums[right] == nums[right + 1]) {
                right--;
            }
            if (left >= right) {
                break;
            }
            const int sum = nums[left] + nums[right];
            if (sum == target) {
                if (idx == capacity) {
                    capacity *= 2;
                    answer = realloc(answer, sizeof(int*) * capacity);
                }
                answer[idx] = malloc(sizeof(int) * 3);
                answer[idx][0] = nums[i];
                answer[idx][1] = nums[left];
                answer[idx][2] = nums[right];
                idx += 1;
                left++;
                right--;
                continue;
            }
            if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
    }
    *returnSize = idx;
    *returnColumnSizes = malloc(sizeof(int) * idx);
    for (int i = 0; i < idx; i++) {
        (*returnColumnSizes)[i] = 3;
    }
    return answer;
}