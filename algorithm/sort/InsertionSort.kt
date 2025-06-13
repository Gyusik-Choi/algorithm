package com.example.sort_kotlin

class InsertionSort {
    fun sort(arr: IntArray) {
        for (i in 1..arr.lastIndex) {
            val numToInsert = arr[i]
            var idx = i
            while (idx > 0 && arr[idx - 1] > numToInsert) {
                arr[idx] = arr[idx - 1]
                idx -= 1
            }
            if (idx != i) {
                arr[idx] = numToInsert
            }
        }
    }
}
