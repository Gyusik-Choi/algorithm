const isCycle = () => {
  for (let i = 1; i < v; i++) {
    if (inDegree[i] > 0) {
      return true;
    }
  }

  return false;
}

const getStartNode = () => {
  const startNode = [];

  for (let i = 1; i <= v; i++) {
    if (!inDegree[i]) {
      startNode.push(i);
    }
  }

  return startNode;
}

const topologySort = () => {
  const answer = [];

  const q = getStartNode();

  while (q.length > 0) {
    const start = q.shift();

    answer.push(start);

    for (const end of edges[start]) {
      inDegree[end] -= 1;

      if (!inDegree[end]) {
        q.push(end);
      }
    }
  }

  if (isCycle()) {
    return [];
  }

  return answer;
}

const input = [
  '7 8',
  '1 2',
  '1 5',
  '2 3',
  '2 6',
  '3 4',
  '4 7',
  '5 6',
  '6 4',
];
// 1 2 5 3 6 4 7

const [v, e] = input.shift().split(' ').map(v => parseInt(v));

const edges = {};

for (let i = 1; i <= v; i++) {
  edges[i] = [];
}

const inDegree = new Array(v + 1).fill(0);

input.forEach(edge => {
  const [s, e] = edge.split(' ').map(e => parseInt(e));
  edges[s].push(e);
  inDegree[e] += 1;
});

console.log(topologySort());
