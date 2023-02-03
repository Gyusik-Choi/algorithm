const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '2 3 2',
//   '1 10',
//   '10 10',
//   '1 2',
//   '1 2 2',
// ];
// => 20

// https://www.acmicpc.net/board/view/107978
// const input = [
//   '4 4 2',
//   '1 2',
//   '3 40',
//   '2 1 1 2',
//   '1 2 2 1',
// ];
// => 80

const [N, M, C] = input.shift().split(' ').map(v => parseInt(v));
const satisfactions = [];

for (let i = 0; i < C; i++) {
  satisfactions.push(input.shift().split(' ').map(v => parseInt(v)));
}

const A = input.shift().split(' ').map(v => parseInt(v));
const B = input.shift().split(' ').map(v => parseInt(v));

const dp = new Array(N + 1).fill(0).map(v => new Array(M + 1).fill(0));

// A 의 1번 학생이 B 의 1번부터 M 번까지 학생과 악수할 경우와
// B 의 1번 학생이 A 의 1번부터 N 번까지 학생과 악수할 경우까지
// 같은 점화식으로 구하기 위해
// dp 배열의 크기를 N + 1, M + 1 사이즈로 구했다
//
// 즉 y 축인 i 가 0인 경우에는 dp[i - 1][j] 가 없고
// x 축인 j 가 0인 경우에는 dp[i][j - 1] 가 없다
// 
// y 축이 0인 경우의 → 방향의 dp 배열 값과
// x 축이 0인 경우의 ↓ 방향의 dp 배열 값을
// B_27212_2 에서는 미리 구했다면
// 여기서는 미리 구하지 않고 같은 점화식으로 계산할 수 있도록
// dp 배열의 크기를 N + 1, M + 1 사이즈로 했다
for (let i = 1; i <= N; i++) {
  for (let j = 1; j <= M; j++) {
    dp[i][j] = Math.max(dp[i - 1][j - 1] + satisfactions[A[i - 1] - 1][B[j - 1] - 1], dp[i - 1][j], dp[i][j - 1]);
  }
}

console.log(dp[N][M]);
