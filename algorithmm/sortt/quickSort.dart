int partition(List<int> arr, int low, int high) {
  int mid = (low + high) ~/ 2;
  int pivot = arr[mid];

  while (low <= high) {
    while (arr[low] < pivot) {
      low += 1;
    }

    while (arr[high] > pivot) {
      high -= 1;
    }

    if (low <= high) {
      int temp = arr[high];
      arr[high] = arr[low];
      arr[low] = temp;
      low += 1;
      high -= 1;
    }
  }

  return low;
}

void split(List<int> arr, int low, int high) {
  if (high - low <= 0) {
    return;
  }

  int mid = partition(arr, low, high);
  split(arr, low, mid - 1);
  split(arr, mid, high);
}

List<int> quickSort(List<int> arr) {
  split(arr, 0, arr.length - 1);
  return arr;
}

void main() {
  List<int> arr = [5, 4, 1, 6, 7, 3, 2];
  List<int> sortedArr = quickSort(arr);
  print(sortedArr);
}