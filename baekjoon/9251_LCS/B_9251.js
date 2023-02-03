const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const firstWord = input[0].split('')
const secondWord = input[1].split('')

const firstWordLength = firstWord.length
const secondWordLength = secondWord.length

let wordArray = new Array(firstWordLength + 1).fill(0).map(v => new Array(secondWordLength + 1).fill(0))

for (let i = 0; i < firstWordLength; i++) {
    const target = firstWord[i]
    for (let j = 0; j < secondWordLength; j++) {
        const candidate = secondWord[j]
        if (target === candidate) {
            wordArray[i + 1][j + 1] = wordArray[i][j] + 1
        } else {
            wordArray[i + 1][j + 1] = Math.max(wordArray[i][j + 1], wordArray[i + 1][j])
        }
    }
}

console.log(wordArray[firstWordLength][secondWordLength])