List<int> countingSort(List<int> arr) {
  // https://stackoverflow.com/questions/20490868/dart-list-min-max-value
  // https://www.cloudhadoop.com/dart-list-min-max-value/
  int maxNum = arr.reduce((a, b) => a >= b ? a : b);

  List<int> maxArr = [];
  List<int> sortedArr = [];

  for (int i = 0; i <= maxNum; i++) {
    maxArr.add(0);
  }

  for (int i = 0; i < arr.length; i++) {
    maxArr[arr[i]] += 1;
    sortedArr.add(0);
  }

  for (int i = 1; i < maxArr.length; i++) {
    maxArr[i] += maxArr[i - 1];
  }

  for (int i = 0; i < arr.length; i++) {
    // arr[i] - arr[i - 1] = arr[i] 의 갯수
    // arr[0] 은 arr[0] 값 자체가 arr[0] 의 갯수
    // 앞의 값을 누적해서 각 인덱스의 값을 구했기 때문에
    // 1을 빼줘야 올바른 인덱스에 값을 넣을 수 있다
    // 즉 0이 1개, 1이 1개라면 [1, 2] 가 된다
    // 0 과 1 이 올바른 위치에 오려면 각 인덱스의 값을 1 뺴준 값이
    // 올바른 인덱스 값이 된다
    maxArr[arr[i]] -= 1;
    int idx = maxArr[arr[i]];
    sortedArr[idx] = arr[i];
  }

  return sortedArr; 
}

void main() {
  List<int> arr = [5, 7, 4, 1, 3, 2, 3, 6, 3, 7, 5, 1];

  if (arr.isNotEmpty) {
    List<int> sortedArr = countingSort(arr);
    print(sortedArr);
  }
}