const binarySearch = (start, end, target) => {
  if (start > end) {
    return;
  }

  const mid = Math.floor((start + end) / 2);

  if (numbers[mid] === target) {
    // 만약 동일한 숫자가 여러개 있는데 
    // 그 중간 지점에서 숫자를 찾으면 
    // 양쪽에 있는 동일한 숫자를 어떻게 찾아야 할지?
    // 찾은 숫자를 기준으로 양쪽 방향 이진 탐색 실행
    cnt += 1;
    binarySearch(start, mid - 1, target);
    binarySearch(mid + 1, end, target);
    return;
  }

  if (numbers[mid] > target) {
    return binarySearch(start, mid - 1, target);
  }

  return binarySearch(mid + 1, end, target);
}

// const [N, x] = [7, 2];
// const numbers = [1, 1, 2, 2, 3, 3, 3];

// const [N, x] = [10, 4];
// const numbers = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4];

const [N, x] = [15, 4];
const numbers = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4];

let cnt = 0;
binarySearch(0, N - 1, x);
console.log(cnt === 0 ? -1 : cnt);
