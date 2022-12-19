const checkChangeInfo = (totalCnt, changeInfo) => {
    return changeInfo.filter(v => v[0] === totalCnt);
}

const move = (arr, changeInfo) => {
    let totalCnt = 0;
    // 최초 오른쪽
    let currentDirection = 1;


    // 상, 우, 하, 좌
    const yValue = [-1, 0, 1, 0];
    const xValue = [0, 1, 0, -1];

    const moveHistory = [[0, 0]];

    while (true) {
        // 뱀 머리 위치
        const headY = moveHistory[moveHistory.length - 1][0];
        const headX = moveHistory[moveHistory.length - 1][1];

        const y = headY + yValue[currentDirection];
        const x = headX + xValue[currentDirection];

        // 벽에 부딪힘
        if (0 > y || y >= N || 0 > x || x >= N) {
            break;
        }
        
        // 자기자신과 부딪힘
        if (arr[y][x] === 0) {
            break;
        }
        
        // 사과가 없으면 꼬리 위치한 칸을 비운다
        if (arr[y][x] < 1) {
            // 뱀 꼬리 위치
            const [tailY, tailX] = moveHistory.shift();

            arr[tailY][tailX] = -1;
        }

        // 뱀 이동
        arr[y][x] = 0;
        moveHistory.push([y, x]);

        totalCnt += 1;

        // 방향 바꿔야 하는지 여부
        // ex> [] -> 시간 정보가 일치하는게 없을 경우
        // ex> [ [ 3, 'D' ] ] -> 시간 정보와 일치하는게 있을 경우
        const change = checkChangeInfo(totalCnt, changeInfo);

        if (change.length === 0) {
            continue;
        }

        const direction = change[0][1];

        // 현재 시간과 방향 변환 초와 일치하면 90도 회전
        // 현재 방향이 0이고 바꿔야할 방향이 왼쪽이면
        // 현재 방향이 3이 되야 하는데
        // -1 을 하고 4의 나머지를 구하면 1이 돼서
        // 직접 3을 대입해준다
        if (currentDirection === 0 && direction === 'L') {
            currentDirection = 3;
        } else {
            if (direction === 'L') {
                currentDirection = (currentDirection - 1) % 4;
            } else {
                currentDirection = (currentDirection + 1) % 4;
            }
        }
    }

    return totalCnt + 1;
}

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = ['6', '3', '3 4', '2 5', '5 3', '3', '3 D', '15 L', '17 D'];
// const input = ['10', '4', '1 2', '1 3', '1 4', '1 5', '4', '8 D', '10 D', '11 D', '13 L'];
// const input = ['10', '5', '1 5', '1 3', '1 2', '1 6', '1 7', '4', '8 D', '10 D', '11 D', '13 L'];

const N = parseInt(input[0]);
const K = parseInt(input[1]);
// -1 빈칸, 0 뱀, 1 사과
// 방문 여부는 고려하지 않는다
const arr = Array.from(Array(N).fill(-1), () => Array(N).fill(-1));

for (let i = 2; i < 2 + K; i++) {
    const [appleY, appleX] = input[i].split(' ').map(v => parseInt(v));
    arr[appleY - 1][appleX - 1] = 1;
}

const L = parseInt(input[2 + K]);
const changeInfo = [];

for (let i = 2 + K + 1; i < 2 + K + 1 + L; i++) {
    const info = input[i].split(' ');
    info[0] = parseInt(info[0]);
    changeInfo.push(info);
}

// 시작점에 뱀 위치
arr[0][0] = 0;
console.log(move(arr, changeInfo));
