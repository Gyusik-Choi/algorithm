package com.example.sort_kotlin

class MergeSort {
    fun sort(arr: IntArray) {
        mergeSort(arr, 0, arr.size - 1)
    }

    private fun mergeSort(arr: IntArray, low: Int, high: Int) {
        if (low >= high) {
            return
        }

        val mid = low + (high - low) / 2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid + 1, high)

        val list = mutableListOf<Int>()
        var l = low
        var m = mid + 1

        while (l <= mid && m <= high) {
            if (arr[l] <= arr[m]) {
                list.add(arr[l])
                l += 1
            } else {
                list.add(arr[m])
                m += 1
            }
        }
        while (l <= mid) {
            list.add(arr[l])
            l += 1
        }
        while (m <= high) {
            list.add(arr[m])
            m += 1
        }

        for (i in list.indices) {
            arr[i + low] = list[i]
        }
    }
}
