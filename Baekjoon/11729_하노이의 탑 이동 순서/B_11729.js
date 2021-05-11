const hanoi = function(N, departure, stopover, destination) {
    if (N === 1) {
        cnt++
        answer += `${departure} ${destination}` + "\n"
    } else {
        hanoi(N - 1, departure, destination, stopover)
        cnt++
        answer += `${departure} ${destination}` + "\n"
        hanoi(N - 1, stopover, departure, destination)
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim()
const K = Number(input)

let cnt = 0
let answer = ''
hanoi(K, '1', '2', '3')

console.log(cnt)
console.log(answer)