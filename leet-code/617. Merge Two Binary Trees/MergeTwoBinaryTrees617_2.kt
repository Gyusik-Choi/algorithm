package com.example

class MergeTwoBinaryTrees617_2 {
    fun mergeTrees(root1: TreeNode?, root2: TreeNode?): TreeNode? {
        if (root1 == null || root2 == null) {
            return root1 ?: root2
        }
        val node = TreeNode(root1.`val` + root2.`val`)
        node.left = mergeTrees(root1.left, root1.left)
        node.right = mergeTrees(root1.right, root2.right)
        return node
    }
}
