/**
 * 마지막으로 정렬이 실행된 인덱스부터는 탐색하지 않는다
 * https://www.algodale.com/algorithms/bubble-sort/
 */
void bubble_sort_3(int *arr, const int size) {
    int end = size - 1;
    while (end > 0) {
        int lastSwappedIdx = 0;
        for (int i = 0; i < end; i++) {
            if (arr[i] > arr[i + 1]) {
                const int temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
                lastSwappedIdx = i;
            }
        }
        end = lastSwappedIdx;
    }
}
