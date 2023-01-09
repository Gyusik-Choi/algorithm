const isEmpty = (arr) => {
    return arr.length === 0;
}

const combination2 = (num, cnt, limit, arr) => {
    if (cnt === limit) {
        answer2 += 1;
        return;
    }

    for (let i = num; i < N; i++) {
        if (isEmpty(arr) || bowlingBalls[arr[arr.length - 1]] !== bowlingBalls[i]) {
            arr.push(i);
            combination2(i + 1, cnt + 1, limit, arr);
            arr.pop();
        }
    }
}

const combination = (limit, n, arr) => {
    if (limit === n) {
        answer += 1;
        return;
    }

    for (let i = 0; i < N; i++) {
        if (isEmpty(arr) || (arr[arr.length - 1] < i && bowlingBalls[arr[arr.length - 1]] !== bowlingBalls[i])) {
            arr.push(i);
            combination(limit, n + 1, arr);
            arr.pop();
        }
        
    }
}

const N = 8;
const M = 5;
const bowlingBalls = [1, 5, 4, 3, 2, 4, 5, 2];

let answer = 0;
let answer2 = 0;
combination(2, 0, []);
combination2(0, 0, 2, []);
console.log(answer);
console.log(answer2);

// 참고
// https://st-lab.tistory.com/115
