List<int> insertionSort(List<int> arr) {
  for (int i = 1; i < arr.length; i++) {
    int idx = i;
    int toInsert = arr[i];

    while (idx > 0 && arr[idx - 1] > toInsert) {
      arr[idx] = arr[idx - 1];
      idx -= 1;
    }

    arr[idx] = toInsert;
  }

  return arr;
}

void main() {
  List<int> arr = [5, 1, 3, 7, 6, 4, 2];
  List<int> sortedArr = insertionSort(arr);
  print(sortedArr);

  List<int> arr2 = [5, 4, 10, 1, 9, 3, 2, 8, 6, 7];
  List<int> sortedArr2 = insertionSort(arr2);
  print(sortedArr2);

  List<int> arr3 = [1];
  List<int> sortedArr3 = insertionSort(arr3);
  print(sortedArr3);
}