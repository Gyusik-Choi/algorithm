void insertion_sort_2(int *arr, const int size) {
    for (int i = 1; i < size; i++) {
        int idx = i;
        while (idx > 0 && arr[idx - 1] > arr[idx]) {
            const int temp = arr[idx];
            arr[idx] = arr[idx - 1];
            arr[idx - 1] = temp;
            idx -= 1;
        }
    }
}
