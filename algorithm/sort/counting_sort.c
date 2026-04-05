#include <stdlib.h>

static int find_biggest(const int* arr, const int size)
{
    int biggest = arr[0];
    for (int i = 1; i < size; i++) {
        if (biggest < arr[i]) {
            biggest = arr[i];
        }
    }
    return biggest;
}

static int find_smallest(const int* arr, const int size)
{
    int smallest = arr[0];
    for (int i = 1; i < size; i++) {
        if (smallest > arr[i]) {
            smallest = arr[i];
        }
    }
    return smallest;
}

/**
 * 호출부에서 free 해야한다
 */
int* counting_sort(const int* arr, const int size)
{
    if (size <= 0) {
        return NULL;
    }
    const int max_number = find_biggest(arr, size);
    // 가장 작은 값을 찾으면 음수에 대비할 수 있고 양수만 배열에 있더라도 배열의 크기를 가능한 작게 유지할 수 있다
    const int offset = find_smallest(arr, size);
    const int max_arr_length = max_number - offset + 1;
    int* max_arr = calloc(max_arr_length,sizeof(int));
    if (max_arr == NULL) {
        return NULL;
    }
    for (int i = 0; i < size; i++) {
        max_arr[arr[i] - offset] += 1;
    }
    for (int i = 1; i < max_arr_length; i++) {
        max_arr[i] += max_arr[i - 1];
    }
    int* answer = calloc(size, sizeof(int));
    if (answer == NULL) {
        free(max_arr);
        return NULL;
    }
    for (int i = 0; i < size; i++) {
        max_arr[arr[i] - offset] -= 1;
        answer[max_arr[arr[i] - offset]] = arr[i];
    }
    free(max_arr);
    return answer;
}
