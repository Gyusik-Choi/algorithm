const N = 5;
const adventurers = [2, 3, 1, 2, 2];
adventurers.sort((a, b) => a - b);

let answer = 0;
let cnt = 0;

let i = 0;
while (i < N) {
    let j = i;

    while (j < N) {
        cnt += 1;

        if (adventurers[j] == cnt) {
            answer += 1;
            cnt = 0;
            break;
        } else {
            j += 1;
        }
    }

    i = j + 1;
}

console.log(answer);
