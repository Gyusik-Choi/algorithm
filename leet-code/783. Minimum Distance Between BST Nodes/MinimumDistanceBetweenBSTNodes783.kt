package com.example

import kotlin.math.min

class MinimumDistanceBetweenBSTNodes783 {
    private var minDistance = 100001
    private var previous = -100001

    fun minDiffInBST(root: TreeNode?): Int {
        inorderTraverse(root)
        return minDistance
    }

    private fun inorderTraverse(root: TreeNode?) {
        if (root!!.left != null) {
            minDiffInBST(root.left)
        }
        minDistance = min(minDistance, root.`val` - previous)
        previous = root.`val`
        if (root.right != null) {
            minDiffInBST(root.right)
        }
    }
}
