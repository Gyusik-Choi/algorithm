void merge(List<int> arr, int low, int mid, int high) {
  int l = low;
  int m = mid + 1;
  List<int> tempArr = [];

  while (l <= mid && m <= high) {
    if (arr[l] < arr[m]) {
      tempArr.add(arr[l]);
      l += 1;
    } else {
      tempArr.add(arr[m]);
      m += 1;
    }
  }

  while (l <= mid) {
    tempArr.add(arr[l]);
    l += 1;
  }

  while (m <= high) {
    tempArr.add(arr[m]);
    m += 1;
  }

  for (int i = 0; i < tempArr.length; i++) {
    arr[i + low] = tempArr[i];
  }
}

void split(List<int> arr, int low, int high) {
  if (high - low <= 0) {
    return;
  }

  int mid = (low + high) ~/ 2;
  split(arr, low, mid);
  split(arr, mid + 1, high);
  merge(arr, low, mid, high);
}

List<int> mergeSort(List<int> arr) {
  split(arr, 0, arr.length - 1);
  return arr;
}

void main() {
  List<int> arr = [5, 4, 1, 6, 7, 3, 2];
  print(mergeSort(arr));
}

// 참고
// https://www.dalecoding.com/algorithms/merge-sort
