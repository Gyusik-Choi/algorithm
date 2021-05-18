const mergeSort = function(low, high) {
    if (high - low < 1) {
        return
    } else {
        mid = Math.floor((low + high) / 2)
        mergeSort(low, mid)
        mergeSort(mid + 1, high)
        
        mergedArr = []
        l = low
        m = mid + 1
        while (l <= mid && m <= high) {
            if (arr[l] < arr[m]) {
                mergedArr.push(arr[l])
                l++
            } else {
                mergedArr.push(arr[m])
                m++
            }
        }

        while (l <= mid) {
            mergedArr.push(arr[l])
            l++
        }

        while (m <= high) {
            mergedArr.push(arr[m])
            m++
        }

        for (let i = 0; i < mergedArr.length; i++) {
            arr[i + low] = mergedArr[i]
        }
    }

}

const arr = [2, 1, 5, 3, 4, 7, 6]
mergeSort(0, arr.length - 1)
console.log(arr)
