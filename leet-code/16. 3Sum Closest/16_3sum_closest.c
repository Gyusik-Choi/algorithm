#include <stdlib.h>

static int compare(const void* a, const void* b) {
    const int x = *(const int*)a;
    const int y = *(const int*)b;
    return (x > y) - (x < y);
}

int threeSumClosest(int* nums, int numsSize, int target) {
    qsort(nums, numsSize, sizeof(int), compare);
    int closest = nums[0] + nums[1] + nums[2];
    for (int i = 0; i < numsSize - 2; i++) {
        if (i > 0 && nums[i - 1] == nums[i]) continue;
        const int min = nums[i] + nums[i + 1] + nums[i + 2];
        if (min > target) {
            if (abs(target - min) < abs(target - closest)) {
                closest = min;
            }
            break;
        }
        const int max = nums[i] + nums[numsSize - 1] + nums[numsSize - 2];
        if (max < target) {
            if (abs(target - max) < abs(target - closest)) {
                closest = max;
            }
            continue;
        }
        int j = i + 1, k = numsSize - 1;
        while (j < k) {
            const int sum = nums[i] + nums[j] + nums[k];
            if (sum == target) return target;
            if (abs(target - sum) < abs(target - closest)) {
                closest = sum;
            }
            if (sum < target) {
                j++;
            } else {
                k--;
            }
        }
    }
    return closest;
}