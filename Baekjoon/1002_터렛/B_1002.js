const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const T = parseInt(input[0])

for (let i = 1; i <= T; i++) {
    arr = input[i].split(' ')
    arr = arr.map(v => Number(v))
    let x1 = arr[0]
    let y1 = arr[1]
    let r1 = arr[2]
    let x2 = arr[3]
    let y2 = arr[4]
    let r2 = arr[5]

    let distance = Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2)
    let rplusDistance = Math.pow(r1 + r2, 2)
    let rminusDistance = Math.pow(r1 - r2, 2)

    if (x1 == x2 && y1 == y2 && r1 == r2) {
        console.log(-1)
    } else if (distance > rplusDistance) {
        console.log(0)
    } else if (distance < rminusDistance) {
        console.log(0)
    } else if (distance === rplusDistance) {
        console.log(1)
    } else if (distance === rminusDistance) {
        console.log(1)
    } else {
        console.log(2)
    }
}