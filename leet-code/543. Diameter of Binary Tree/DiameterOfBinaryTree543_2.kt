package com.example

import kotlin.math.max

class DiameterOfBinaryTree543_2 {
    fun diameterOfBinaryTree(root: TreeNode?): Int {
        var diameter = 0
        fun dfs(node: TreeNode?): Int {
            if (node == null) {
                return 0
            }
            val left = dfs(node.left)
            val right = dfs(node.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1
        }
        dfs(root)
        return diameter
    }
}
