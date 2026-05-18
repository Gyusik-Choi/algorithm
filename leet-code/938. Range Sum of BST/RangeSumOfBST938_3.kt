package com.example

class RangeSumOfBST938_3 {
    fun rangeSumBST(root: TreeNode?, low: Int, high: Int): Int {
        if (root == null) return 0
        val leftSums = if (root.`val` <= low) 0 else rangeSumBST(root.left, low, high)
        val rightSums = if (root.`val` >= high) 0 else rangeSumBST(root.right, low, high)
        return leftSums + rightSums + (if (root.`val` in low..high) root.`val` else 0)
    }
}
