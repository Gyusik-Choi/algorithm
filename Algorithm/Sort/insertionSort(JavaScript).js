const changeItems = function(i, minIdx) {
    const temp = arr[i]
    arr[i] = arr[minIdx]
    arr[minIdx] = temp
}

const insertionSort = function(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        let minIdx = i
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[minIdx] > arr[j]) {
                minIdx = j
            }
        }
        
        // i보다 더 작은 인덱스를 찾았다면
        if (i != minIdx) {
            changeItems(i, minIdx)
        }
    }
}

let arr = [2, 1, 5, 3, 4, 7, 6, 8, 10, 9]
insertionSort(arr)
console.log(arr)