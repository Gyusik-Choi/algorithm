class InvertBinaryTree226_5 {
    fun invertTree(root: TreeNode?): TreeNode? {
        if (root == null) return null
        root.left = root.right.also { root.right = root.left }
        invertTree(root.left)
        invertTree(root.right)
        return root
    }
}
