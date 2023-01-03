const solution = (N, stages) => {
  // 오름차순 정렬
  stages.sort((a, b) => a - b);

  // 사용자 수
  let players = stages.length;
  // 동일 스테이지 사용자 수
  let stageCnt = 0;
  // stages 를 for loop 할 시작 인덱스
  let startIdx = 0;
  // 실패율
  let failRate = [];

  // 1 부터 N 까지
  // N + 1 은 구해야할 실패율 범위에 포함되지 않아서 확인하지 않아도 된다
  for (let stage = 1; stage <= N; stage++) {
    // startIdx 부터 stages 길이 - 1 만큼 for loop
    for (let idx = startIdx; idx < stages.length; idx++) {
      if (stage === stages[idx]) {
        stageCnt += 1;
        continue;
      }

      startIdx = idx;
      break;
    }
    
    // 안쪽 for 문을 끝까지 돌고 그대로 끝나버린 경우가 있어서
    // failRate, players, stageCnt 처리를 
    // break 문 위에서 하지 않고 여기서 수행
    failRate.push([stageCnt / players, stage]);
    players -= stageCnt;
    stageCnt = 0;
  }

  return failRate.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : b[0] - a[0]).map(v => v[1]);
}

console.log(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]));
console.log(solution(4, [4, 4, 4, 4, 4]));
console.log(solution(3, [4, 1, 1, 1, 4]));
