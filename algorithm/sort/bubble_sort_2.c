#include <stdbool.h>

/**
 * 배열 내 자리 이동이 더 이상 발생하지 않으면
 * 정렬이 완료됐다는 의미라 for loop 종료
 * https://www.algodale.com/algorithms/bubble-sort/
 */
void bubble_sort_2(int *arr, const int size) {
    for (int i = size - 1; i > 0; i--) {
        bool is_switched = false;
        for (int j = 0; j < i; j++) {
            if (arr[j] > arr[j + 1]) {
                const int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                is_switched = true;
            }
        }
        if (!is_switched) {
            break;
        }
    }
}
