package com.example.sort_kotlin

class QuickSort {
    fun sort(arr: IntArray): IntArray {
        return quickSort(arr, 0, arr.size - 1)
    }

    private fun quickSort(arr: IntArray, low: Int, high: Int): IntArray {
        if (low < high) {
            val pivot = partition(arr, low, high)
            quickSort(arr, low, pivot - 1)
            quickSort(arr, pivot + 1, high)
        }
        return arr
    }

    private fun partition(arr: IntArray, low: Int, high: Int): Int {
        val pivot = arr[high]
        var left = low
        for (right in low until high) {
            if (arr[right] < pivot) {
                swap(arr, left, right)
                left += 1
            }
        }
        // for 문을 다 돌고나서 left 와 high 의 값을 교환한다
        // for 문에서 매번 arr[right] 보다 pivot 이 더 컸다면
        // left 가 계속 증가해서 high 가 동일해진다
        // 그러면 여기서 swap 을 하더라도 요소 위치는 변경되지 않는다
        // left 가 high 와 동일하지 않다는 의미는
        // left 가 가리키는 값이 pivot 보다 크다는 뜻이다
        // left 와 high 를 교환해서 left 까지는 pivot 보다
        // 작거나 같은 값만 있음을 보장한다
        // 아래의 swap 으로 인해 left 위치에는 pivot 값이 오게 된다
        // 그래서 여기서 left 를 리턴하고
        // 이 left 를 받은 val pivot = partition(arr, low, high) 를 보면
        // left 를 pivot 으로 받는다 그리고 pivot 을 제외한
        // left ~ pivot - 1, pivot + 1 ~ high 범위를 재귀 호출한다
        swap(arr, left, high)
        return left
    }

    private fun swap(arr: IntArray, i: Int, j: Int) {
        val temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    }
}
