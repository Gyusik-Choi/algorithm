class MergeTwoBinaryTrees617_2 {
    fun mergeTrees(root1: TreeNode?, root2: TreeNode?): TreeNode? {
        if (root1 == null) return root2
        if (root2 == null) return root1
        val newNode = TreeNode(root1.`val` + root2.`val`)
        newNode.left = mergeTrees(root1.left, root2.left)
        newNode.right = mergeTrees(root1.right, root2.right)
        return newNode
    }
}
