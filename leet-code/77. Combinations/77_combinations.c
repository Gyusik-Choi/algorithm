#include <stdlib.h>

static int* copy_arr(const int* arr, const int size)
{
    int* copied_arr = malloc(size * sizeof(int));
    for (int i = 0; i < size; i++) {
        copied_arr[i] = arr[i];
    }
    return copied_arr;
}

static void getCombinations(int** combs, int* combsIdx, int* comb, const int combIdx, const int numLimit, const int num, const int sizeLimit)
{
    if (combIdx == sizeLimit) {
        combs[*combsIdx] = copy_arr(comb, sizeLimit);
        (*combsIdx)++;
        return;
    }
    for (int i = num; i <= numLimit; i++) {
        comb[combIdx] = i;
        getCombinations(combs, combsIdx, comb, combIdx + 1, numLimit, i + 1, sizeLimit);
    }
}

static int getMin(const int a, const int b)
{
    return (a < b) ? a : b;
}

static int getNumberOfCombinations(const int n, const int k)
{
    // int numerator = 1;
    // for (int i = n; i > n - k; i--) {
    //     numerator *= i;
    // }
    // int denominator = 1;
    // for (int i = 1; i <= k; i++) {
    //     denominator *= i;
    // }
    // return numerator / denominator;
    // 위의 방식은 오버플로우가 발생했다
    // n 이 20이고 k 가 10일 때 20부터 11까지 곱하면 약 6천억이 넘는다
    int result = 1;
    for (int i = 0; i < getMin(n - k, k); i++) {
        result = result * (n - i) / (i + 1);
    }
    return result;
}

/**
* Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** combine(int n, int k, int* returnSize, int** returnColumnSizes)
{
    *returnSize = getNumberOfCombinations(n, k);
    *returnColumnSizes = malloc(*returnSize * sizeof(int));
    int** answer = malloc(*returnSize * sizeof(int*));
    for (int i = 0; i < *returnSize; i++) {
        (*returnColumnSizes)[i] = k;
        
    }
    int combsIdx = 0;
    int* comb = malloc(k * sizeof(int));
    getCombinations(answer, &combsIdx, comb, 0, n, 1, k);
    free(comb);
    return answer;
}
