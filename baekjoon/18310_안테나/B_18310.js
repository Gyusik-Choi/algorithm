const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '4',
//   '5 1 7 9',
// ];
// => 5

// const input = [
//   '5',
//   '1 3 5 5 5',
// ]
// => 5

const N = parseInt(input[0]);

const houses = input[1].split(' ').map(v => parseInt(v));
houses.sort((a, b) => a - b);

const centerIdx = N % 2 === 0 ? Math.floor(N / 2) - 1 : Math.floor(N / 2);
console.log(houses[centerIdx]);
