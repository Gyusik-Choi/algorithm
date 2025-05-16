import kotlin.math.max

class DiameterOfBinaryTree543_2 {
    fun diameterOfBinaryTree(root: TreeNode?): Int {
        var maxDiameter = 1

        fun dfs(node: TreeNode?): Int {
            if (node == null) return 0
            val left = dfs(node.left)
            val right = dfs(node.right)
            maxDiameter = max(maxDiameter, left + right + 1)
            return max(left, right) + 1
        }

        dfs(root)
        return maxDiameter - 1
    }
}
