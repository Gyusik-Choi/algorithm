package com.example.sort_kotlin

class MergeSort {
    /**
     * 파라미터 arr 을 정렬
     */
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

    /**
     * 파라미터 arr 을 정렬하지 않고 별도의 배열로 정렬해서 반환
     */
    fun sort2(arr: IntArray): IntArray {
        val low = 0
        val high = arr.size - 1

        if (low >= high) {
            return arr
        }

        val mid = low + (high - low) / 2
        val lowArr = sort2(arr.slice(IntRange(low, mid)).toIntArray())
        val highArr = sort2(arr.slice(IntRange(mid + 1, high)).toIntArray())

        val list = IntArray(arr.size)
        var idx = 0
        var l = 0
        var h = 0
        while (l <= lowArr.size - 1 && h <= highArr.size - 1) {
            if (lowArr[l] <= highArr[h]) {
                list[idx] = lowArr[l]
                l += 1
            } else {
                list[idx] = highArr[h]
                h += 1
            }
            idx += 1
        }
        while (l <= lowArr.size - 1) {
            list[idx] = lowArr[l]
            l += 1
            idx += 1
        }
        while (h <= highArr.size - 1) {
            list[idx] = highArr[h]
            h += 1
            idx += 1
        }

        return list
    }
}
