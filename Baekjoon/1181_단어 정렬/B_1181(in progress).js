const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
let words = []
for (let i = 1; i <= N; i++) {
    let temp = []
    const word = input[i]
    const length = word.length
    temp.push(word)
    temp.push(length)
    words.push(temp)
}

const sortedWords = words.sort((a, b) => {
    if (a[1] < b[1]) {
        return -1
    }
})

const sortedSameLengthWords = []
let idx = 0
while (idx < sortedWords.length) {
    let temp = [sortedWords[idx][0]]
    let flag = false
    for (let i = idx + 1; i < sortedWords.length; i++) {
        if (temp[0].length === sortedWords[i][1]) {
            if (temp.indexOf(sortedWords[i][0]) === -1) {
                temp.push(sortedWords[i][0])
            } else {
                continue
            }
        } else {
            idx = i
            break
        }
        
        if (i === sortedWords.length - 1) {
            flag = true
        }
    }

    temp.sort()
    for (let k = 0; k < temp.length; k++) {
        sortedSameLengthWords.push(temp[k])    
    }

    if (flag) {
        break
    }
    
}

let answer = ''
for (let i = 0; i < sortedSameLengthWords.length; i++) {
    const ans = sortedSameLengthWords[i]
    answer += ans + '\n'
}

console.log(answer)