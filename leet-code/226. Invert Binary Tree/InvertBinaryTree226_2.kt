package com.example

class InvertBinaryTree226_2 {
    fun invertTree(root: TreeNode?): TreeNode? {
        if (root == null) {
            return null
        }
        val left = root.left
        root.left = invertTree(root.right)
        root.right = invertTree(left)
        return root
    }
}
