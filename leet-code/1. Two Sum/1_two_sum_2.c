#include <stdlib.h>

typedef struct {
    int value;
    int index;
} Pair ;

static int compare(const void* a, const void* b) {
    const Pair* x = a;
    const Pair* y = b;
    return (x->value > y->value) - (x->value < y->value);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    Pair* pairs = malloc(sizeof(Pair) * numsSize);
    for (int i = 0; i < numsSize; i++) {
        pairs[i].value = nums[i];
        pairs[i].index = i;
    }

    qsort(pairs, numsSize, sizeof(Pair), compare);

    int* answer = malloc(sizeof(int) * 2);
    int left = 0, right = numsSize - 1;
    *returnSize = 0;
    while (left < right) {
        const Pair a = pairs[left];
        const Pair b = pairs[right];
        const int sum = a.value + b.value;
        if (sum == target) {
            answer[0] = a.index;
            answer[1] = b.index;
            *returnSize = 2;
            break;
        }
        if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    free(pairs);
    return answer;
}
