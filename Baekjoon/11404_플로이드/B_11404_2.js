const floydWarshall = () => {
  for (let i = 0; i < n; i++) {
    costs[i][i] = 0;
  }

  for (let k = 0; k < n; k++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        costs[i][j] = Math.min(costs[i][k] + costs[k][j], costs[i][j]);
      }
    }
  }
}

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '5',
//   '14',
//   '1 2 2',
//   '1 3 3',
//   '1 4 1',
//   '1 5 10',
//   '2 4 2',
//   '3 4 1',
//   '3 5 1',
//   '4 5 3',
//   '3 5 10',
//   '3 1 8',
//   '1 4 2',
//   '5 1 7',
//   '3 4 2',
//   '5 2 4',
// ];

const n = parseInt(input.shift());
const m = parseInt(input.shift());
const costs = new Array(n).fill(Infinity).map(v => new Array(n).fill(Infinity));

input.forEach((v) => {
  const [a, b, c] = v.split(' ').map(v => parseInt(v));

  costs[a - 1][b - 1] = Math.min(costs[a - 1][b - 1], c);
});

floydWarshall();

console.log(costs.map(cost => cost.map(c => c === Infinity ? '0' : c.toString()).join(' ')).join('\n'));
