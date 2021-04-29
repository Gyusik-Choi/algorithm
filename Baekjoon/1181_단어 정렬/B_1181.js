const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
let minLength = Infinity
let maxLength = -Infinity

let words = []
for (let i = 1; i <= N; i++) {
    const word = input[i]
    words.push(word)

    const length = word.length
    if (length > maxLength) {
        maxLength = length
    }

    if (length < minLength) {
        minLength = length
    }
}

const sortedWords = []
for (let i = minLength; i <= maxLength; i++) {
    let temp = []
    for (let j = 0; j < words.length; j++) {
        if (words[j].length === i && temp.indexOf(words[j]) === -1) {
            temp.push(words[j])
        }
    }
    temp.sort()
    for (let k = 0; k < temp.length; k++) {
        sortedWords.push(temp[k])
    }
}

let answer = ''
for (let i = 0; i < sortedWords.length; i++) {
    const ans = sortedWords[i]
    answer += ans + '\n'
}

console.log(answer)