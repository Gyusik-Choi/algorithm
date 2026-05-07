package com.example

class InvertBinaryTree226_3 {
    fun invertTree(root: TreeNode?): TreeNode? {
        if (root == null) {
            return null
        }
        val left = root.left
        root.left = root.right
        root.right = left
        invertTree(root.left)
        invertTree(root.right)
        return root
    }
}
