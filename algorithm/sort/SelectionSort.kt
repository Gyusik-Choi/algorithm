package com.example.sort_kotlin

class SelectionSort {
    fun sort(arr: IntArray) {
        for (i in 0 until arr.size - 1) {
            println(i)
            var idx = i
            for (j in i until arr.size) {
                if (arr[idx] > arr[j]) {
                    idx = j
                }
            }
            if (i != idx) {
                swap(arr, i, idx)
            }
        }
    }

    private fun swap(arr: IntArray, i: Int, j: Int) {
        val temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    }
}
