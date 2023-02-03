List<int> bubbleSort(List<int> arr) {
  int length = arr.length;

  if (length == 1) {
    return arr;
  }

  for (int i = length - 1; i > 0; i--) {
    for (int j = 0; j < i; j++) {
      if (arr[j] > arr[j + 1]) {
        int temp = arr[j + 1];
        arr[j + 1] = arr[j];
        arr[j] = temp;
      }
    }
  }

  return arr;
}

void main() {
  List<int> arr = [5, 4, 3, 2, 1];
  List<int> sortedArr = bubbleSort(arr);
  print(sortedArr);

  List<int> arr2 = [5, 4];
  List<int> sortedArr2 = bubbleSort(arr2);
  print(sortedArr2);

  List<int> arr3 = [5];
  List<int> sortedArr3 = bubbleSort(arr3);
  print(sortedArr3);
}