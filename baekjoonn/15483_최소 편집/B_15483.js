const getMinimumEditDistance = () => {
  for (let i = 1; i < secondWord.length + 1; i++) {
    dp[i][0] = i;
  }

  for (let j = 1; j < firstWord.length + 1; j++) {
    dp[0][j] = j;
  }

  for (let i = 1; i < secondWord.length + 1; i++) {
    for (let j = 1; j < firstWord.length + 1; j++) {
      if (secondWord[i - 1] === firstWord[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1];
      } else {
        dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1;
      }
    }
  }
}

const setDp = () => {
  const dp = [];

  for (let i = 0; i < secondWord.length + 1; i++) {
    const dpOneLine = [];
    
    for (let j = 0; j < firstWord.length + 1; j++) {
      dpOneLine.push(0);
    }

    dp.push(dpOneLine);
  }

  return dp;
}

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = ['abc', 'ab'];

// const input = ['ca', 'abc'];

// const input = ['abc', 'cba'];

// const input = ['abcd', 'bcde'];

// const input = ['abababababa', 'aaaaaaaaaaa'];

// const input = ['for', 'whileforif'];

// const input = ['abcdef', 'azced'];

// const input = ['asdf', 'asdf'];

// const input = ['aaabaaa', 'acacaca'];

const firstWord = input[0];
const secondWord = input[1];

const dp = setDp();

getMinimumEditDistance();

console.log(dp[secondWord.length][firstWord.length]);
