const buildRouter = (distance) => {
  let cnt = 1;

  let start = houses[0];

  for (let i = 1; i < N; i++) {
    const end = houses[i];

    if (end - start >= distance) {
      cnt += 1;
      start = end;
    }
  }

  return cnt;
}

const binarySearch = (low, high) => {
  // 이번 문제에서는 
  // low 와 high 가 같은 경우도 검사해줘야 해서
  // low < high 가 아니라
  // low <= high 로 하면서
  // low <= high 가 무한 루프에 빠지지 않도록
  // high = mid 가 아니라
  // high = mid - 1 로 했다
  while (low <= high) {
    mid = Math.floor((low + high) / 2);

    const totalRouters = buildRouter(mid);

    if (totalRouters >= C) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  
  return low - 1;
}

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '5 3',
//   '1',
//   '2',
//   '8',
//   '4',
//   '9',
// ];

// const input = [
//   '9 3',
//   '1',
//   '2',
//   '3',
//   '4',
//   '5',
//   '6',
//   '7',
//   '8',
//   '100'
// ];
// => 7 (1, 8, 100)

// const input = [
//   '2 2',
//   '0',
//   '1',
// ]
// => 1

// const input = [
//   '3 3',
//   '1',
//   '3',
//   '4',
// ];
// => 1

// https://www.acmicpc.net/board/view/68339
// const input = [
//   '5 2',
//   '1',
//   '2',
//   '4',
//   '8',
//   '9'
// ];
// 8

// https://www.acmicpc.net/board/view/78328
// const input = [
//   '4 3',
//   '11',
//   '13',
//   '16',
//   '18',
// ];
// => 2

// https://www.acmicpc.net/board/view/77951
// const input = [
//   '5 3',
//   '1',
//   '7',
//   '8',
//   '9',
//   '10'
// ];
// => 3

const [N, C] = input[0].split(' ').map(v => parseInt(v));
input.shift();

const houses = input.map(v => parseInt(v)).sort((a, b) => a - b);

if (N === 2) {
  console.log(houses[1] - houses[0]);
} else {
  // console.log(binarySearch(houses[1] - houses[0], houses[N - 1] - houses[0]));
  // 시작점을 위와 같이 잘못 잡아서 오답이 나왔었다
  console.log(binarySearch(1, houses[N - 1] - houses[0]));
}
