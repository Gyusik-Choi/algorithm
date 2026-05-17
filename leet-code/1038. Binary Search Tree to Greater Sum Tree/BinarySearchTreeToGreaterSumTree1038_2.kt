package com.example

class BinarySearchTreeToGreaterSumTree1038_2 {
    private var sums = 0

    fun bstToGst(root: TreeNode?): TreeNode? {
        if (root == null) {
            return null
        }
        bstToGst(root.right)
        root.`val` += sums
        sums = root.`val`
        bstToGst(root.left)
        return root
    }
}
