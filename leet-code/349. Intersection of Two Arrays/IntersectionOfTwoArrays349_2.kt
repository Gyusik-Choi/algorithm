package com.example

class IntersectionOfTwoArrays349_2 {
    fun intersection(nums1: IntArray, nums2: IntArray): IntArray {
        nums1.sort()
        val set = mutableSetOf<Int>()
        nums2.forEach { if (exist(nums1, it)) set.add(it) }
        return set.toIntArray()
    }

    private fun exist(arr: IntArray, num: Int): Boolean {
        var low = 0
        var high = arr.lastIndex
        while (low <= high) {
            val mid = low + (high - low) / 2
            when {
                arr[mid] < num -> low = mid + 1
                arr[mid] > num -> high = mid - 1
                else -> return true
            }
        }
        return false
    }
}
