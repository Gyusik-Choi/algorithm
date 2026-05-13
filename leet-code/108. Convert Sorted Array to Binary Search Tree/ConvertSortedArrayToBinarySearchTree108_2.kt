package com.example

class ConvertSortedArrayToBinarySearchTree108_2 {
    fun sortedArrayToBST(nums: IntArray): TreeNode? {
        if (nums.isEmpty()) {
            return null
        }
        val mid = nums.size / 2
        val node = TreeNode(nums[mid])
        if (mid > 0) {
            node.left = sortedArrayToBST(nums.sliceArray(IntRange(0, mid - 1)))
        }
        if (mid + 1 < nums.size) {
            node.right = sortedArrayToBST(nums.sliceArray(IntRange(mid + 1, nums.size - 1)))
        }
        return node
    }
}
