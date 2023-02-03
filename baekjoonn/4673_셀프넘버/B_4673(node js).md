# 백준

## 4673

```javascript
let arr = new Array(10001)
arr.fill(1)

for (let i = 1; i < 10001; i++) {
    selfNum(i)
}

function selfNum(number) {
    let total = number
    if (arr[number] != 0) {
        while (total < 10000) {
            let nums = total
            while (nums != 0) {
                total += nums % 10
                nums = parseInt(nums / 10)
            }
            arr[total] = 0
        }
    }
}

for (let j = 1; j < 10001; j++) {
    if (arr[j] === 1) {
        console.log(j)
    }
}
```

