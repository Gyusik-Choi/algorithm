void change(List<int> arr, int idx1, int idx2) {
  int temp = arr[idx1];
  arr[idx1] = arr[idx2];
  arr[idx2] = temp;
}

List<int> selectionSort(List<int> arr) {
  for (int i = 0; i < arr.length - 1; i++) {
    int minIdx = i;

    for (int j = i + 1; j < arr.length; j++) {
      if (arr[minIdx] > arr[j]) {
        minIdx = j;
      }
    }

    if (i != minIdx) {
      change(arr, i, minIdx);
    }
  }

  return arr;
}

void main() {
  List<int> arr = [5, 1, 3, 6, 7, 4, 2];
  List<int> sortedArr = selectionSort(arr);
  print(sortedArr);

  List<int> arr2 = [2, 1];
  List<int> sortedArr2 = selectionSort(arr2);
  print(sortedArr2);

  List<int> arr3 = [1];
  List<int> sortedArr3 = selectionSort(arr3);
  print(sortedArr3);
}