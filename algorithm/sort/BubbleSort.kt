package com.example.sort_kotlin

class BubbleSort {
    fun sort(arr: IntArray) {
        for (i in arr.size - 2 downTo 0) {
            for (j in 0..i) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr, j, j + 1)
                }
            }
        }
    }

    fun sort2(arr: IntArray) {
        for (i in 1..arr.size - 1) {
            for (j in 0..arr.size - 1 - i) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr, j, j + 1)
                }
            }
        }
    }

    fun sort3(arr: IntArray) {
        for (i in arr.size - 2 downTo 0) {
            var swapped = false
            for (j in 0..i) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr, j, j + 1)
                    swapped = true
                }
            }
            if (!swapped) {
                break
            }
        }
    }

    private fun swap(arr: IntArray, i: Int, j: Int) {
        val temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    }
}
