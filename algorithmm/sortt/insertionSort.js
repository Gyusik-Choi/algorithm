const changeItem = function(firstIdx, secondIdx) {
    const temp = arr[firstIdx]
    arr[firstIdx] = arr[secondIdx]
    arr[secondIdx] = temp
}

const insertionSort2 = function() {
    for (let i = 1; i < arr.length; i++) {
        let idx = i
        let toInsert = arr[i]
        while (idx > 0 && arr[idx - 1] > toInsert) {
            arr[idx] = arr[idx - 1]
            idx -= 1
        }
        arr[idx] = toInsert
    }
}

const insertionSort = function() {
    for (let i = 1; i < arr.length; i += 1) {
        for (let j = i; j > 0; j -= 1) {
            if (arr[j - 1] > arr[j]) {
                changeItem(j - 1, j)
            } else {
                break
            }
        }
    }
}

let arr = [2, 5, 1, 3, 4]
insertionSort2(arr)
console.log(arr)