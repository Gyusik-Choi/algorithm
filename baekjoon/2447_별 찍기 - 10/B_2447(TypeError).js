const fs = require("fs")
const N = Number(fs.readFileSync("/dev/stdin").toString().trim())

const arr = new Array(N).fill("").map(() => new Array(N).fill(""));

const makeStar = function(y, x, M) {
    if (M === 1) {
        arr[y][x] = "*"
        return
    } else {
        let n = M / 3
        for (let k = 0; k < 3; k++) {
            for (let l = 0; l < 3; l++) {
                if (k === 1 && l === 1) {
                    continue
                } else {
                    makeStar(y * M + k, x * M + l, n)
                }
            }
        }
    }
}

makeStar(0, 0, N)

let star = ""
for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
        star += arr[i][j]
    }
    star += "\n"
}
console.log(star)