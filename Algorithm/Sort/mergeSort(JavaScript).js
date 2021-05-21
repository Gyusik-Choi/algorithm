// 정말 주의할점은 변수에 var, let, const 등의 선언을 하지 않으면
// node 환경에서는 global에 포함된다
// 함수 안의 스코프에 포함되는게 아니라 
// 전역에 포함돼서 재귀의 상황에 맞춰서 값이 변화하지 않고
// 전역에 선언한 것에 맞춰서 정해진다

const mergeSort = function(low, high) {
    if (high - low < 1) {
        return
    } else {
        const mid = Math.floor((low + high) / 2)
        mergeSort(low, mid)
        mergeSort(mid + 1, high)
        
        let mergedArr = []
        let l = low
        let m = mid + 1
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
