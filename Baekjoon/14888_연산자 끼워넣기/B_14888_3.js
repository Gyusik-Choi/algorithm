const getMaxAndMinValue = (numbers, operators) => {
  // maxValue 를 음수가 나올 수 있음을 간과하고
  // 처음에 0 으로 했으나 0 으로 하면 안 된다
  let maxValue = -Infinity;
  let minValue = Infinity;
  let cntLimit = N - 1;

  const [plus, minus, multiply, division] = operators

  const getCombinations = (plus, minus, multiply, division, cnt, sums) => {
    if (cnt === cntLimit) {
      // -0 이 나올 수 있음에 주의
      if (sums === -0) {
        sums = 0;
      }

      maxValue = Math.max(maxValue, sums);
      minValue = Math.min(minValue, sums);
      return;
    }

    const targetNumber = numbers[cnt + 1];

    if (plus) {
      getCombinations(plus - 1, minus, multiply, division, cnt + 1, sums + targetNumber);
    }
  
    if (minus) {
      getCombinations(plus, minus - 1, multiply, division, cnt + 1, sums - targetNumber);
    }
  
    if (multiply) {
      getCombinations(plus, minus, multiply - 1, division, cnt + 1, sums * targetNumber);
    }
  
    if (division) {
      getCombinations(plus, minus, multiply, division - 1, cnt + 1, sums < 0 ? Math.ceil(sums / targetNumber) : Math.floor(sums / targetNumber));
    }
  }

  getCombinations(plus, minus, multiply, division, 0, numbers[0]);
  return [maxValue, minValue];
}

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '2',
//   '5 6',
//   '0 0 1 0'
// ];

// const input = [
//   '3',
//   '3 4 5',
//   '1 0 1 0',
// ];

// const input = [
//   '6',
//   '1 2 3 4 5 6',
//   '2 1 1 1'
// ];

const N = parseInt(input[0]);
const numbers = input[1].split(' ').map(v => parseInt(v));
const operators = input[2].split(' ').map(v => parseInt(v));

const [maxVal, minVal] = getMaxAndMinValue(numbers, operators);
console.log(maxVal);
console.log(minVal);
