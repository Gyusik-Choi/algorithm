let arr = [2, 1, 5, 3, 4]

for (let i = arr.length - 1; i > -1; i--) {
    for (let j = 0; j <= i; j++) {
        if (arr[j] > arr[j + 1]) {
            const temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
        }
    }
}

console.log(arr)