package com.example

import kotlin.math.max

class MaximumDepthOfBinaryTree104_2 {
    fun maxDepth(root: TreeNode?): Int {
        if (root == null) return 0
        return max(maxDepth(root.left), maxDepth(root.right)) + 1
    }
}
