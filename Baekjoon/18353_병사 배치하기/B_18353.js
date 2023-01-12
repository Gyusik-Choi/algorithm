const binarySearch = (low, high, target) => {
  while (low < high) {
    mid = Math.floor((low + high) / 2);

    // soldiers 로 하지 않도록 주의!
    if (lds[mid] < target) {
      high = mid;
    } else {
      low = mid + 1;
    }
  }

  return low;
}

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '7',
//   '15 11 4 8 5 2 4'
// ];
// => 2

// const input = [
//   '8',
//   '15 11 9 8 5 2 4 6'
// ];
// => 2

// https://www.acmicpc.net/board/view/90743
// const input = [
//   '12',
//   '12 2 5 3 2 10 8 7 15 5 4 3'
// ];
// => 5
// 15 10 8 7 5 4 3

const N = parseInt(input.shift());
const soldiers = input[0].split(' ').map(v => parseInt(v));

const lds = [];
soldiers.forEach(soldier => {
  if (lds.length === 0 || lds[lds.length - 1] > soldier) {
    lds.push(soldier);
  } else {
    const idx = binarySearch(0, lds.length - 1, soldier);

    lds[idx] = soldier;
  }
});

console.log(N - lds.length);
