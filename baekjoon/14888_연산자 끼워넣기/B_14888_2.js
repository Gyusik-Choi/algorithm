const calc = function({idx, sums, p, s, m, d}) {
    if (idx === N - 1) {
        // -0은 0이 되도록 처리
        if (sums === -0) {
            sums = 0
        }

        if (maxNum < sums) {
            maxNum = sums
        }

        if (minNum > sums) {
            minNum = sums
        }
    } else {
        if (p > 0) {
            calc({
                idx: idx + 1,
                sums: sums + numbers[idx + 1],
                p: p - 1,
                s,
                m,
                d
            })
        }

        if (s > 0) {
            calc({
                idx: idx + 1,
                sums: sums - numbers[idx + 1],
                p,
                s: s - 1,
                m,
                d
            })
        }

        if (m > 0) {
            calc({
                idx: idx + 1,
                sums: sums * numbers[idx + 1],
                p,
                s,
                m: m - 1,
                d
            })
        }

        if (d > 0) {
            // 양수나 0이면 내림
            if (sums >= 0) {
                sums = Math.floor(sums / numbers[idx + 1])
            // 음수면 올림
            } else {
                sums = Math.ceil(sums / numbers[idx + 1])
            }
            calc({
                idx: idx + 1,
                sums,
                p,
                s,
                m,
                d: d - 1
            })
        }
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = Number(input[0])
const numbers = input[1].split(' ').map(v => Number(v))
const operators = input[2].split(' ').map(v => Number(v))

let maxNum = -Infinity
let minNum = Infinity

calc({
    idx: 0,
    sums: numbers[0],
    p: operators[0],
    s: operators[1],
    m: operators[2],
    d: operators[3]
})

console.log(maxNum)
console.log(minNum)

// 참고
// https://www.youtube.com/watch?v=Jz8Sx1XYb04
// 노마드코더의 clean code 관련 영상으로 인자가 많은 경우에는 object로 보내는 것을 추천한다는 내용에 영향을 받았다