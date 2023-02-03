// bfs 로 방문하면서
// 최단거리면서 거리 K 를 만족하는 정점을 찾는다
const bfs = (go, targetDistance) => {
  // 최단 거리 정보 => 시작점 0, 나머지 -1
  // 최단 거리 정보가 -1 이 아니면 방문을 이미 한 걸로 간주
  // bfs 로 방문하므로 처음에 갱신된 거리가 최단 거리다
  const distances = new Array(N + 1).fill(-1);
  distances[go] = 0;

  // 방문 큐
  const queue = [go];
  const cityNums = [];

  // https://www.acmicpc.net/source/32640553
  // 이분의 풀이를 보고 아이디어를 얻어서
  // queue.shift() 를 사용하지 않고
  // queue 의 idx 를 올려가면서 접근하는 방식으로 변경해서
  // 시간초과를 해결
  let idx = 0;

  while (queue.length > idx) {
    const start = queue[idx];
    // const start = queue.shift();

    for (let i = 0; i < edges[start].length; i++) {
      const end = edges[start][i];
      // 아직 방문하지 않은 도시
      if (distances[end] === -1) {
        queue.push(end);
        distances[end] = distances[start] + 1;

        if (distances[end] === targetDistance) {
          cityNums.push(end);
        }
      }
    }

    idx += 1;
  }

  if (cityNums.length === 0) {
    cityNums.push(-1);
  }

  return cityNums.sort((a, b) => a - b);
}

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '4 4 2 1',
//   '1 2',
//   '1 3',
//   '2 3',
//   '2 4'
// ];

// const input = [
//   '4 3 2 1',
//   '1 2',
//   '1 3',
//   '1 4'
// ];

// const input = [
//   '4 4 1 1',
//   '1 2',
//   '1 3',
//   '2 3',
//   '2 4'
// ];

// const input = [
//   '2 2 2 1',
//   '1 2',
//   '2 1'
// ]
// => -1

const [N, M, K, X] = input[0].split(' ').map(v => parseInt(v));
input.shift();

const cities = input.map(v => v.split(' ').map(v => parseInt(v)));

// 간선 정보
const edges = [];
for (let i = 0; i <= N; i++) {
  edges.push([]);
}

cities.forEach((v, i) => {
  const [s, e] = v;
  edges[s].push(e);
});

bfs(X, K).forEach((v, i) => console.log(v));
