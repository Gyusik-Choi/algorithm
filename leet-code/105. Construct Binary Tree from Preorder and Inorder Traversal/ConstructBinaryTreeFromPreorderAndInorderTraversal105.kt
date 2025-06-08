package com.example

class ConstructBinaryTreeFromPreorderAndInorderTraversal105 {
    fun buildTree(preorder: IntArray, inorder: IntArray): TreeNode? {
        val preOrder = mutableListOf<Int>()
        val inOrder = mutableListOf<Int>()
        for (p in preorder) {
            preOrder.add(p)
        }
        for (i in inorder) {
            inOrder.add(i)
        }
        return dfs(preOrder, inOrder)
    }

    fun dfs(preOrder: MutableList<Int>, inOrder: MutableList<Int>): TreeNode? {
        if (inOrder.isEmpty()) {
            return null
        }
        val parent = TreeNode(preOrder.first())
        val idx = inOrder.indexOf(preOrder.first())
        parent.left = dfs(preOrder.subList(1, idx + 1), inOrder.subList(0, idx))
        parent.right = dfs(preOrder.subList(idx + 1, preOrder.size), inOrder.subList(idx + 1, inOrder.size))
        return parent
    }
}
