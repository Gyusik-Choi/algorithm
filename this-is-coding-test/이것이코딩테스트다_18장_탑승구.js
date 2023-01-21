class DisjointSet {
  constructor(n) {
    this.parent = new Array(n + 1).fill(0);
    this.makeSet(n);
  }

  makeSet(n) {
    for (let i = 0; i <= n; i++) {
      this.parent[i] = i;
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

    if (px === 0) {
      return false;
    }

    if (px === py) {
      this.parent[py] = px - 1;
      return true;
    }

    return this.unionSet(x - 1, y);
  }
}

// const input = [
//   '4',
//   '3',
//   '4',
//   '1',
//   '1',
// ];
// => 2

const input = [
  '4',
  '6',
  '2',
  '2',
  '3',
  '3',
  '4',
  '4',
];
// // => 3

const G = parseInt(input.shift());
const P = parseInt(input.shift());

const gates = [];

for (let i = 0; i < P; i++) {
  // 탑승구 번호를 0 ~ G - 1 로 하기 위해
  gates.push(parseInt(input.shift()));
}

const disjointSet = new DisjointSet(G);

let answer = 0;

for (const gate of gates) {
  if (!disjointSet.unionSet(gate, gate)) {
    break;
  }

  answer += 1;
}

console.log(answer);

// maksSet 으로 초기화한 DisjointSet 의
// parent 배열의 값을
// 어떻게 처리해서 도킹 여부를 판단할지 의문
