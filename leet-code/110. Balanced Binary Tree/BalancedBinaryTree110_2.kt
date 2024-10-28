package com.example

import kotlin.math.abs
import kotlin.math.max

class BalancedBinaryTree110_2 {
    fun isBalanced(root: TreeNode?): Boolean {
        return searchTree(root) != -1
    }

    private fun searchTree(node: TreeNode?): Int {
        if (node == null) return 0
        val left = searchTree(node.left)
        val right = searchTree(node.right)
        if (left == -1 || right == -1 || abs(left - right) > 1) return -1
        return max(left, right) + 1
    }
}
