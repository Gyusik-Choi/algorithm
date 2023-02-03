const findMaxItem = function(lst) {
    let maxItem = -Infinity
    for (let i = 0; i < lst.length; i++) {
        if (lst[i] > maxItem) {
            maxItem = lst[i]
        }
    }
    return maxItem
}

const countingSort = function(lst, maxNum) {
    let maxArr = new Array(maxNum + 1).fill(0)
    let newArr = new Array(lst.length).fill(0)

    for (let i = 0; i < lst.length; i++) {
        maxArr[lst[i]] += 1
    }

    for (let i = 1; i < maxArr.length; i++) {
        maxArr[i] += maxArr[i - 1]
    }

    for (let i = 0; i < newArr.length; i++) {
        maxArr[arr[i]] -= 1
        const item = maxArr[arr[i]]
        newArr[item] = arr[i]
        
        // 아래처럼 하면 안 된다.
        // maxArr[arr[i]]의 값 자체를 1 감소시켜야 하는데
        // maxArr[arr[i]] 값 자체는 변하지 않고 item2 변수에만 1이 감소된 값이 들어가게 되기 때문이다.

        // const item2 = maxArr[arr[i]] - 1
        // newArr[item2] = arr[i]
    }
    return newArr
    
}

let arr = [2, 2, 1, 1, 5, 5, 3, 4, 4, 3]
const maxItem = findMaxItem(arr)
const sortedArr = countingSort(arr, maxItem)
console.log(sortedArr)
