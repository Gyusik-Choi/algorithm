const isCycle = (n, degree) => {
  for (let i = 1; i < n; i++) {
    if (degree[i] > 0) {
      return true;
    }
  }

  return false;
}

const getStartNode = (n, degree) => {
  const startNode = [];

  for (let i = 1; i <= n; i++) {
    if (!degree[i]) {
      startNode.push(i);
    }
  }

  return startNode;
}

const topologySort = (n, degree, grade) => {
  const answer = [];

  const q = getStartNode(n, degree);
  
  while (q.length > 0) {
    const start = q.shift();

    answer.push(start.toString());

    for (let end = 1; end <= n; end++) {
      if (grade[start][end]) {
        degree[end] -= 1;

        if (!degree[end]) {
          q.push(end);
        }
      }
    }
  }

  if (isCycle(n, degree)) {
    return 'IMPOSSIBLE';
  }

  return answer.join(' ');
}

// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const input = [
  '3',
  '5',
  '5 4 3 2 1',
  '2',
  '2 4',
  '3 4',
  '3',
  '2 3 1',
  '0',
  '4',
  '1 2 3 4',
  '3',
  '1 2',
  '3 4',
  '2 3',
];

// const input = [
//   '1',
//   '3',
//   '2 3 1',
//   '0',
// ];

const t = parseInt(input[0]);

let idx = 1;

for (let i = 0; i < t; i++) {
  const n = parseInt(input[idx]);

  idx += 1;

  const inDegree = new Array(n + 1).fill(0);

  const grades = new Array(n + 1).fill(0).map(v => new Array(n + 1).fill(0));

  const lastGrades = input[idx].split(' ').map(v => parseInt(v));

  for (let i = 0; i < n - 1; i++) {
    const f = lastGrades[i];

    for (let j = i + 1; j < n; j++) {
      const g = lastGrades[j];

      inDegree[g] += 1;
      grades[f][g] = 1;
    }
  }

  idx += 1;

  const m = parseInt(input[idx]);

  idx += 1;

  const gradeChangedTeams = [];

  if (m > 0) {
    for (let j = idx; j < idx + m; j++) {
      const changedTeams = input[j].split(' ').map(v => parseInt(v))
  
      gradeChangedTeams.push(changedTeams);
  
      const [f, g] = changedTeams;
  
      if (grades[f][g]) {
        grades[f][g] = 0;
        grades[g][f] = 1;
  
        inDegree[g] -= 1;
        inDegree[f] += 1;
      } else {
        grades[f][g] = 1;
        grades[g][f] = 0;
  
        inDegree[g] += 1;
        inDegree[f] -= 1;
      }
    }
  
    idx += m;
  }

  console.log(topologySort(n, inDegree, grades));
}

// https://deque.tistory.com/62

// disjoint-set 을 생각했으나
// 이는 포함 관계를 정리하기 위한
// 부분 집합이 필요할때 사용하기에 적절하나
// 이번 문제처럼 우선 순위를 판단해야할 문제에는
// 위상정렬을 사용하는게 적절하다
