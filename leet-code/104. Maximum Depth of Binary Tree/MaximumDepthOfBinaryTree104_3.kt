import kotlin.math.max

class MaximumDepthOfBinaryTree104_3 {
    fun maxDepth(root: TreeNode?): Int {
        if (root == null) return 0
        val left = maxDepth(root.left)
        val right = maxDepth(root.right)
        return max(left, right) + 1
    }
}
