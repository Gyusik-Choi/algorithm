package com.example

import kotlin.math.max

class LongestUnivaluePath687_2 {
    private var maxUnivaluePath = 0

    fun longestUnivaluePath(root: TreeNode?): Int {
        findLongestUnivaluePath(root)
        return maxUnivaluePath
    }

    private fun findLongestUnivaluePath(root: TreeNode?): Int {
        if (root == null) {
            return 0
        }
        val left = findLongestUnivaluePath(root.left)
        val right = findLongestUnivaluePath(root.right)
        if (root.left != null && root.left.`val` == root.`val` && root.right != null && root.`val` == root.right.`val`) {
            maxUnivaluePath = max(maxUnivaluePath, left + right + 2)
            return max(left, right) + 1
        }
        if (root.left != null && root.left.`val` == root.`val`) {
            maxUnivaluePath = max(maxUnivaluePath, left + 1)
            return left + 1
        }
        if (root.right != null && root.right.`val` == root.`val`) {
            maxUnivaluePath = max(maxUnivaluePath, right + 1)
            return right + 1
        }
        return 0
    }
}
