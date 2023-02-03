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
        
        let possible_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        // 가로
        for (let i = 0; i < 9; i++) {
            const row_idx = arr[y][i]
            possible_arr[row_idx] = 0
        }
        
        //세로
        for (let i = 0; i < 9; i++) {
            const ver_idx = arr[i][x]
            possible_arr[ver_idx] = 0
        }

        // 사각형
        let vertical = Math.floor(y / 3) * 3
        let horizontal = Math.floor(x / 3) * 3
        for (let i = vertical; i < vertical + 3; i++) {
            for (let j = horizontal; j < horizontal + 3; j++) {
                const square_idx = arr[i][j]
                possible_arr[square_idx] = 0
            }
        }

        let candidates = []
        for (let i = 0; i < possible_arr.length; i++) {
            if (possible_arr[i] !== 0) {
                candidates.push(possible_arr[i])
            }
        }

        for (let i = 0; i < candidates.length; i++) {
            const candidate = candidates[i]
            arr[y][x] = candidate
            check(idx + 1)
            arr[y][x] = 0
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