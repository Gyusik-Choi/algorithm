package com.example.sort_kotlin

class CountingSort {
    fun sort(arr: IntArray): IntArray {
        if (arr.isEmpty()) {
            return IntArray(0)
        }
        val maxNum = arr.max()
        val newArr = IntArray(maxNum + 1)
        for (num in arr) {
            newArr[num] += 1
        }
        for (i in 1.. newArr.size - 1) {
            newArr[i] += newArr[i - 1]
        }
        val sortedArr = IntArray(arr.size)
        for (i in arr.indices) {
            newArr[arr[i]] -= 1
            sortedArr[newArr[arr[i]]] = arr[i]
        }
        return sortedArr

        // [3 3 5 5 2]
        // [0 0 0 0 0 0]
        // [0 0 1 2 0 2]
        // [0 0 1 3 3 5]
        // [0 0 0 0 0]
        // [0 0 1 2 3 5] -> [0 0 3 0 0]
        // [0 0 1 1 3 5] -> [0 3 3 0 0]
        // [0 0 1 1 3 4] -> [0 3 3 0 5]
        // [0 0 1 1 3 3] -> [0 3 3 5 5]
        // [0 0 0 1 3 3] -> [2 3 3 5 5]
    }
}
