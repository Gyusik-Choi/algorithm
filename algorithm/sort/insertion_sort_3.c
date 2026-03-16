void insertion_sort_3(int *arr, const int size) {
    for (int i = 1; i < size; i++) {
        const int to_insert = arr[i];
        int idx = i;
        while (idx > 0 && arr[idx - 1] > to_insert) {
            arr[idx] = arr[idx - 1];
            idx -= 1;
        }
        arr[idx] = to_insert;
    }
}
