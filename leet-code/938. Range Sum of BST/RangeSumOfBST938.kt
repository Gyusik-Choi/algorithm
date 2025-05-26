package com.example

class RangeSumOfBST938 {
    fun rangeSumBST(root: TreeNode?, low: Int, high: Int): Int {
        if (root == null) {
            return 0
        }

        var sum = 0
        sum += rangeSumBST(root.left, low, high)
        sum += rangeSumBST(root.right, low, high)
        if (low <= root.`val` && root.`val` <= high) {
            sum += root.`val`
        }
        return sum
    }
}
