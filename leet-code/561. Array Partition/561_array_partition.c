#include <stdlib.h>

static int compare(const void* a, const void* b) {
    const int x = *(const int*)a;
    const int y = *(const int*)b;
    return (x > y) - (x < y);
}

int arrayPairSum(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), compare);
    int pair_sum = 0;
    for (int i = 0; i < numsSize; i += 2) {
        pair_sum += nums[i];
    }
    return pair_sum;
}
