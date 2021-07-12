const changeItem = function(first, second) {
    const temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp
}

const partition = function(low, high) {
    // pivot을 Math.floor((low + high) / 2)로만 한다면 pivot 값이 low와 high가 바뀌면서 계속 변동이 일어나기 때문에 하나의 값으로 고정하기 위해 arr[Math.floor((low + high) / 2)]로 설정
    // Math.floor는 소수점 없이 몫만 구하기 위해 사용
    const pivot = arr[Math.floor((low + high) / 2)]
    while (low <= high) {

        while (pivot > arr[low]) {
            low += 1
        }

        while (pivot < arr[high]) {
            high -= 1
        }

        if (low <= high) {
            changeItem(low, high)
            low += 1
            high -= 1
        }
    }

    return low
}

const quickSort = function(low, high) {
    if (high <= low) {
        return
    }

    mid = partition(low, high)
    quickSort(low, mid - 1)
    quickSort(mid, high)
}

let arr = [2, 1, 5, 3, 7, 6, 4]
quickSort(0, arr.length - 1)
console.log(arr)
