const bubbleSort = (lst) => {
  const arr = [...lst];

  for (let i = arr.length - 1; i > -1; i--) {
    for (let j = 0; j <= i; j++) {
      if (arr[j] > arr[j + 1]) {
        const temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp
      }
    }
  }

  return arr;
}

const arr = [2, 1, 5, 4, 3];
const sortedArr = bubbleSort(arr);
console.log(sortedArr);
