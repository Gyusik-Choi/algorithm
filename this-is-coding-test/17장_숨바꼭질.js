const bfs = (go) => {
  const q = [go];

  while (q.length > 0) {
    const start = q.shift();

    for (const end of barnObj[start]) {
      if (!distances[end][1] && end > 1) {
        distances[end][1] = distances[start][1] + 1;
        q.push(end);
      }
    }
  }
}

const input = [
  '6 7',
  '3 6',
  '4 3',
  '3 2',
  '1 3',
  '1 2',
  '2 4',
  '5 2',
];

const [N, M] = input.shift().split(' ').map(v => parseInt(v));
const barnInfo = input.map(v => v.split(' ').map(v => parseInt(v)));

const barnObj = {};

for (let i = 1; i <= N; i++) {
  barnObj[i] = [];
}

barnInfo.forEach(v => {
  const [A, B] = v;

  barnObj[A].push(B);
  barnObj[B].push(A);
});

const distances = [];

for (let i = 0; i <= N; i++) {
  distances.push([i, 0])
}

bfs(1);

distances.sort((a, b) => {
  if (a[1] === b[1]) {
    return a[0] - b[0];
  }

  return b[1] - a[1];
})

const barnNumberToHide = distances[0][0];

const maxDistance = distances[0][1];

let sameMaxDistanceCnt = 0;

for (const [barnNumber, dist] of distances) {
  if (dist === maxDistance) {
    sameMaxDistanceCnt += 1;
  } else {
    break;
  }
}

console.log(barnNumberToHide, maxDistance, sameMaxDistanceCnt);
