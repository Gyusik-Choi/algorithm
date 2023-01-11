const setDp = (arr) => {
  for (let i = 1; i <= n; i++) {
    arr.push(Array.from(Array(i).fill(0)));
  }

  return arr;
}

const getMaxValue = () => {
  for (let i = 1; i < n; i++) {
    for (let j = 0; j < dp[i].length; j++) {
      if (j === 0) {
        dp[i][j] = dp[i - 1][j] + triangle[i][j];
        continue;
      }

      if (j === i) {
        dp[i][j] = dp[i - 1][j - 1] + triangle[i][j];
        continue;
      }

      dp[i][j] = Math.max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j];
    }
  }

  return dp;
}


const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '5',
//   '7',
//   '3 8',
//   '8 1 0',
//   '2 7 4 4',
//   '4 5 2 6 5'
// ];
// => 30

const n = parseInt(input[0]);
input.shift();

const triangle = input.map(v => v.split(' ').map(v => parseInt(v)));
const dp = setDp([]);
dp[0][0] = triangle[0][0]

getMaxValue();
console.log(Math.max(...dp[n - 1]));
