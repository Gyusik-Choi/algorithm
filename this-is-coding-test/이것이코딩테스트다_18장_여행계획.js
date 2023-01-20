class DisjointSet {
  constructor(n) {
    this.parent = new Array(n).fill(0);
    this.makeSet(n);
  }

  makeSet(n) {
    for (let i = 0; i < n; i++) {
      this.parent[i] = i
    }
  }

  findSet(x) {
    if (this.parent[x] !== x) {
      this.parent[x] = this.findSet(this.parent[x]);
    }

    return this.parent[x];
  }

  unionSet(x, y) {
    const px = this.findSet(x);
    const py = this.findSet(y);

    this.parent[py] = px;
  }
}

const getAnswer = () => {
  for (let i = 0; i < M - 1; i++) {
    if (disjointSet.findSet(i) !== disjointSet.findSet(i + 1)) {
      return 'NO';
    }
  }

  return 'YES';
}

const input = [
  '5 4',
  '0 1 0 1 1',
  '1 0 1 1 0',
  '0 1 0 0 0',
  '1 1 0 0 0',
  '1 0 0 0 0',
  '2 3 4 3',
];
// => YES

// const input = [
//   '6 4',
//   '0 1 1 0 0 0',
//   '1 0 0 0 0 0',
//   '1 0 0 0 0 0',
//   '0 0 0 0 1 0',
//   '0 0 0 1 0 1',
//   '0 0 0 0 1 0',
//   '3 4',
// ];
// => NO

const [N, M] = input.shift().split(' ').map(v => parseInt(v));
const roads = [];

for (let i = 0; i < N; i++) {
  roads.push(input.shift().split(' ').map(v => parseInt(v)));
}

// 0 ~ N - 1 로 전체 범위를 잡으면서
// 여행 계획의 숫자를 정수로 변환한 뒤 1을 빼준다
const plans = input.shift().split(' ').map(v => parseInt(v) - 1);

const roadsAdj = {};

for (let i = 0; i < N; i++) {
  roadsAdj[i] = [];
}

const disjointSet = new DisjointSet(N);

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (roads[i][j]) {
      // i, j 와 j, i 는 양방향으로 연결된다
      // 중복해서 unionSet 을 수행하지 않도록
      // i, j 의 부모 노드가 같으면
      // unionSet 을 수행하지 않는다
      if (disjointSet.findSet(i) !== disjointSet.findSet(j)) {
        disjointSet.unionSet(i, j);
      }
    }
  }
}

console.log(getAnswer());
