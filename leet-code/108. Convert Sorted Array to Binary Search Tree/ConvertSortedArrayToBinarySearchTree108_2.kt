package com.example

class ConvertSortedArrayToBinarySearchTree108_2 {
    fun sortedArrayToBST(nums: IntArray): TreeNode? {
        fun sliceList(list: List<Int>, start: Int, end: Int): List<Int> {
            return list.slice(start..end).toMutableList()
        }

        fun createBST(nums: List<Int>): TreeNode? {
            if (nums.isEmpty()) return null
            val mid = (nums.size - 1) / 2
            val node = TreeNode(nums[mid])
            val leftChild = createBST(sliceList(nums, 0, mid - 1))
            val rightChild = createBST(sliceList(nums, mid + 1, nums.size - 1))
            node.left = leftChild
            node.right = rightChild
            return node
        }

        return createBST(nums.toList())
    }
}
