#include <stdlib.h>

static int* copy_arr(int* arr, const int size)
{
    int* copied_arr = malloc(size * sizeof(int));
    for (int i = 0; i < size; i++) {
        copied_arr[i] = arr[i];
    }
    return copied_arr;
}

static void recursion(int* nums, const int numsSize, int** perms, int* perm, int* used, int* permsIdx, int permIdx)
{
    if (numsSize == permIdx) {
        perms[*permsIdx] = copy_arr(perm, numsSize);
        (*permsIdx)++;
        return;
    }
    for (int i = 0; i < numsSize; i++) {
        if (used[i] == 1) {
            continue;
        }
        perm[permIdx] = nums[i];
        used[i] = 1;
        recursion(nums, numsSize, perms, perm, used, permsIdx, permIdx + 1);
        used[i] = 0;
    }
}

static int factorial(const int n)
{
    int fac = 1;
    for (int i = 1; i <= n; i++) {
        fac *= i;
    }
    return fac;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes)
{
    *returnSize = factorial(numsSize);
    *returnColumnSizes = malloc(*returnSize * sizeof(int));
    int** answer = malloc(*returnSize * sizeof(int*));
    for (int i = 0; i < *returnSize; i++) {
        (*returnColumnSizes)[i] = numsSize;
        // 아래는 생략 가능하다.
        // 2차원 배열에서 내부에 1차원 배열의 주소값을 넣을 공간에 대한 동적할당은
        // 위의 int** answer = malloc(*returnSize * sizeof(int*)); 에서 이미 적용됐다.
        // copy_arr 함수 내부에서 실제 int 데이터 공간을 할당하고 int 값들을 넣은 뒤에
        // 해당 공간에 대한 주소값을 반환하고 이 주소값을 perms[*permsIdx] 에 할당한다.
        // answer[i] = malloc(numsSize * sizeof(int));
    }
    int* permutation = malloc(numsSize * sizeof(int));
    int* use = calloc(numsSize, sizeof(int));
    int permsIdx = 0;
    recursion(nums, numsSize, answer, permutation, use, &permsIdx, 0);
    free(permutation);
    free(use);
    return answer;
}
