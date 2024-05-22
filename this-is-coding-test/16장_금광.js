const setMine = () => {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      mine[i][j] = mineInfo[(i * m) + j];
    }
  }
}

const setFirstDpColumn = () => {
  for (let i = 0; i < n; i++) {
    dp[i][0] = mine[i][0];
  }
}

const getMaxDp = () => {
  // 한 열을 모두 끝내고 다음 열로 이동해야 해서
  // 기존의 i, j 의 순서와 다르게 진행한다
  for (let j = 1; j < m; j++) {
    for (let i = 0; i < n; i++) {
      if (i === 0) {
        dp[i][j] = Math.max(dp[i][j - 1], dp[i + 1][j - 1]) + mine[i][j];
        continue;
      }

      if (i === n - 1) {
        dp[i][j] = Math.max(dp[i - 1][j - 1], dp[i][j - 1]) + mine[i][j];
        continue;
      }

      dp[i][j] = Math.max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1]) + mine[i][j];
    }
  }

  return _getMaxValueOfLastDpColumn();
}

const _getMaxValueOfLastDpColumn = () => {
  let maxValue = dp[0][m - 1];

  for (let i = 1; i < n; i++) {
    maxValue = Math.max(maxValue, dp[i][m - 1]);
  }

  return maxValue;
}

// const [n, m] = [3, 4];
// const mineInfo = [
//   1, 3, 3, 2, 
//   2, 1, 4, 1, 
//   0, 6, 4, 7,
// ];
// => 19

const [n, m] = [4, 4];
const mineInfo = [
  1, 3, 1, 5, 
  2, 2, 4, 1, 
  5, 0, 2, 3, 
  0, 6, 1, 2,
]
// => 16

const mine = Array.from(Array(n), () => Array(m).fill(0));
setMine();

const dp = Array.from(Array(n), () => Array(m).fill(0));
setFirstDpColumn();

console.log(getMaxDp());
