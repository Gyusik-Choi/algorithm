const isKnowCorrectGrade = (n) => {
  for (let i = 1; i <= N; i++) {
    // 본인 번호가 아니면서
    if (n !== i) {
      // 둘 다 Infinity 면 정확한 성적을 알 수 없어서 return false
      // 하나라도 Infinity 가 아니면 두 번호 간의 성적이 어디가 더 높은 지 알 수 있다는 의미
      if (grade[i][n] === Infinity && grade[n][i] === Infinity) {
        return false;
      }
    }
  }

  // 하나라도 false 로 걸리지 않고 여기로 왔다는 것은
  // n 에 대해서 정확한 순위를 알 수 있다는 의미
  return true;
}

const getAnswer = () => {
  let answer = 0;

  for (let i = 1; i <= N; i++) {
    if (isKnowCorrectGrade(i)) {
      answer += 1;
    }
  }

  return answer;
}

const floydWarshall = () => {
  for (let k = 1; k <= N; k++) {
    for (let i = 1; i <= N; i++) {
      for (let j = 1; j <= N; j++) {
        grade[i][j] = Math.min(grade[i][j], grade[i][k] + grade[k][j]);
      }
    }
  }
}

const input = [
  '6 6',
  '1 5',
  '3 4',
  '4 2',
  '4 6',
  '5 2',
  '5 4',
];

const [N, M] = input.shift().split(' ').map(v => parseInt(v));
const grade = Array(N + 1).fill(Infinity).map(v => new Array(N + 1).fill(Infinity));
const gradeInfo = input.map(g => g.split(' ').map(g => parseInt(g)));

for (let i = 0; i <= N; i++) {
  grade[i][i] = 0;
}

// 낮은 -> 높은
gradeInfo.forEach(g => {
  grade[g[0]][g[1]] = 1;
});

floydWarshall();

console.log(getAnswer());
