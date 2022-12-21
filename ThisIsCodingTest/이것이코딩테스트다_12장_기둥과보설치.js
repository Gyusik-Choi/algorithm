const sortCallBack = (a, b) => {
  if (a[0] === b[0]) {
    if (a[1] === b[1]) {
      return a[2] - b[2];
    }

    return a[1] - b[1];
  }

  return a[0] - b[0];
};

const isPillarPossible = (buildHistory, y, x) => {
  // 바닥 위
  if (y === 0) {
    return true;
  }

  // 보의 한쪽 끝 부분 위
  if (buildHistory.filter(v => (v[0] === x - 1 && v[1] === y && v[2] === 1) || (v[0] === x && v[1] === y && v[2] === 1)).length > 0) {
    return true;
  }
  

  // 다른 기둥 위
  if (buildHistory.filter(v => v[0] === x && v[1] === y - 1 && v[2] === 0).length > 0) {
    return true;
  }

  return false;
}

const isBeamPossible = (buildHistory, y, x) => {
  // 한쪽 끝 부분이 기둥 위
  // 왼쪽 끝에 기둥 혹은 오른쪽 끝에 기둥
  if (buildHistory.filter(v => (v[0] === x && v[1] === y - 1 && v[2] === 0) || (v[0] === x + 1 && v[1] === y - 1 && v[2] === 0)).length > 0) {
    return true;
  }

  // 양쪽 끝 부분이 다른 보와 동시에 연결
  // 양쪽 끝 부분을 만족해야 해서 filter 로 나온 결과값 배열의 길이가 2 이상이어야 한다
  if (buildHistory.filter(v => (v[0] === x - 1 && v[1] === y && v[2] === 1) || (v[0] === x + 1 && v[1] === y && v[2] === 1)).length > 1) {
    return true;
  }

  return false;
}

const isValidBuild = (buildHistory) => {
  for (const build of buildHistory) {
    const [x, y, a] = build;

    // 기둥
    if (a === 0) {
      if (!isPillarPossible(buildHistory, y, x)) {
        return false;
      }

      // 여기서 끊지 않으면 밑의 if 문으로 들어간다
      continue;
    }

    // 보
    if (!isBeamPossible(buildHistory, y, x)) {
      return false;
    }
  }

  return true;
}

const solution = (n, buildFrame) => {
  // 정답을 담은 배열이면서 동시에
  // 조건 만족하는지를 판단하기 위해 이전의 설치 혹은 삭제한 목록을 갖고 있음
  let buildHistory = [];

  // 일단 설치하거나 삭제한 다음에
  // 전체 요소들이 조건을 만족하는지 확인하고
  // 조건을 만족하지 못하면 원래데로 돌아간다
  buildFrame.forEach((v, i) => {
    // 가로, 세로, 구조물(0 기둥, 1 보), 설치 or 삭제(1 or 0)
    const [x, y, a, b] = v;

    // 설치
    if (b === 1) {
      buildHistory.push([x, y, a]);

      if (!isValidBuild(buildHistory)) {
        buildHistory = buildHistory.filter(v => v[0] !== x || v[1] !== y || v[2] !== a);
      }
    // 삭제
    } else {
      buildHistory = buildHistory.filter(v => v[0] !== x || v[1] !== y || v[2] !== a);

      if (!isValidBuild(buildHistory)) {
        buildHistory.push([x, y, a]);
      }
    }
  });

  // 정렬 후 반환
  return buildHistory.sort(sortCallBack);
}

console.log(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]));
console.log(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]));
