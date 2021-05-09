const makeStars = function(N, y, x) {
    if (N === 1) {
        stars[y][x] = '*'
    } else {
        N = Math.ceil(N / 3)
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                if (i === 1 && j === 1) {
                    continue
                } else {
                    makeStars(N, i * N + y, j * N + x)
                }
            }
        }
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString()
const N = Number(input)

let stars = new Array(N).fill("").map(() => new Array(N).fill(""))
makeStars(N, 0, 0)
let answer = ""
for (let k = 0; k < N; k++) {
    const temp = stars[k].join("")
    answer += temp + "\n"
}
console.log(answer)