const bfs = (go) => {
  const q = [go];

  const yValue = [-1, 0, 1, 0];
  const xValue = [0, 1, 0, -1];

  while (q.length > 0) {
    const [y, x] = q.shift();

    for (let k = 0; k < 4; k++) {
      const yIdx = (y + yValue[k] + N) % N;
      const xIdx = (x + xValue[k] + M) % M;

      if (0 > yIdx || yIdx >= N || 0 > xIdx || xIdx >= M) {
        continue;
      }

      if (!planet[yIdx][xIdx]) {
        planet[yIdx][xIdx] = 1;
        q.push([yIdx, xIdx]);
      }
    }
  }
}

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '5 6',
//   '1 1 1 1 1 1',
//   '1 0 0 0 1 1',
//   '1 1 1 1 0 0',
//   '1 1 1 1 0 0',
//   '1 1 1 1 1 1',
// ];
// => 2

// const input = [
//   '7 8',
//   '0 0 1 1 0 0 0 0',
//   '0 1 1 1 1 0 1 0',
//   '1 1 1 1 1 1 1 1',
//   '0 1 1 1 1 1 0 0',
//   '1 1 0 0 0 1 0 0',
//   '0 1 0 0 0 1 0 1',
//   '0 0 1 1 1 1 0 0',
// ];
// => 2

const [N, M] = input.shift().split(' ').map(v => parseInt(v));
const planet = input.map(v => v.split(' ').map(v => parseInt(v)));

let cnt = 0;

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (!planet[i][j]) {
      planet[i][j] = 1;
      cnt += 1;

      bfs([i, j]);
    }
  }
}

console.log(cnt);
