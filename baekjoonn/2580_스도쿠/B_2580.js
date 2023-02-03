const squareCheck = function(v, h, n) {
    if (v < 3) {
        v = 0
    } else if (v < 6) {
        v = 3
    } else {
        v = 6
    }

    if (h < 3) {
        h = 0
    } else if (h < 6) {
        h = 3
    } else {
        h = 6
    }

    for (let i = v; i < v + 3; i++) {
        for (let j = h ; j < h + 3; j++) {
            if (arr[i][j] === n) {
                return 0
            }
        }
    }
    return 1
}

const columnCheck = function(v, h, n) {
    for (let i = 0; i < 9; i++) {
        if (arr[i][h] === n) {
            return 0
        }
    }
    return 1
}

const rowCheck = function(v, h, n) {
    for (let i = 0; i <= 9; i++) {
        if (arr[v][i] === n) {
            return 0
        }
    }
    return 1
}

const check = function(idx) {
    if (idx === zeroArr.length) {
        for (let i = 0; i < 9; i++) {
            console.log(arr[i].join(" "))
        }
        process.exit(0);
    } else {
        let item = zeroArr[idx]
        let y = item[0]
        let x = item[1]
        for (let i = 1; i <= 9; i++) {
            if (rowCheck(y, x, i) === 1 && columnCheck(y, x, i) === 1 && squareCheck(y, x, i) === 1) {
                arr[y][x] = i
                check(idx + 1)
                arr[y][x] = 0
            } 
        }
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const arr = new Array(9).fill(0).map(v => new Array(9).fill(0))
for (let i = 0; i < 9; i++) {
    let input_lst = input[i].split(' ')
    let lst = input_lst.map(v => Number(v))
    for (let j = 0; j < 9; j++) {
        arr[i][j] = lst[j]
    }
}

let zeroArr = []
for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
        if (arr[i][j] === 0) {
            zeroArr.push([i, j])
        }
    }
}

check(0)