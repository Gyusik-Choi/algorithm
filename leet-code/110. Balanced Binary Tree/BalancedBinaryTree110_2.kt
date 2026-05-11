package com.example

import kotlin.math.abs
import kotlin.math.max

class BalancedBinaryTree110_2 {
    fun isBalanced(root: TreeNode?): Boolean {
        return dfs(root) != -1
    }

    private fun dfs(node: TreeNode?): Int {
        if (node == null) {
            return 0
        }
        val left = dfs(node.left)
        val right = dfs(node.right)
        if (left == -1 || right == -1 || abs(left - right) >= 2) {
            return -1
        }
        return max(left, right) + 1
    }
}
