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

const dp = new Array(N).fill(0).map(v => new Array(M).fill(0));

dp[0][0] = satisfactions[A[0] - 1][B[0] - 1];

// A 의 1번 학생 (dp 배열의 인덱스로는 0) 이 
// B 의 1번부터 M 번 학생과 (dp 배열의 인덱스로는 0부터 M - 1)
// 악수할 경우의 최대값을 구한다
// 
// A 의 1번 학생에 대한 경우라 x 축 값은 0 으로 고정됐다
for (let i = 1; i < N; i++) {
  dp[i][0] = Math.max(dp[i - 1][0], satisfactions[A[i] - 1][B[0] - 1]);
}

// B 의 1번 학생 (dp 배열의 인덱스로는 0) 이 
// A 의 1번부터 N 번 학생과 (dp 배열의 인덱스로는 0부터 N - 1)
// 악수할 경우의 최대값을 구한다
// 
// B 의 1번 학생에 대한 경우라 y 축 값은 0으로 고정됐다
for (let j = 1; j < M; j++) {
  dp[0][j] = Math.max(dp[0][j - 1], satisfactions[A[0] - 1][B[j] - 1]);
}

// A 의 1번부터 N 번 학생이
// B 의 1번부터 M 번 학생과
// 악수할 경우의 최대값 구한다
for (let i = 1; i < N; i++) {
  for (let j = 1; j < M; j++) {
    dp[i][j] = Math.max(dp[i - 1][j - 1] + satisfactions[A[i] - 1][B[j] - 1], dp[i - 1][j], dp[i][j - 1]);
  }
}

console.log(dp[N - 1][M - 1]);
