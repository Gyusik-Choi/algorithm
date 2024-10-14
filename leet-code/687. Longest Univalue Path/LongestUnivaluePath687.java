public class LongestUnivaluePath687 {
    private int longestUnivalue = 1;

    public int longestUnivaluePath(TreeNode root) {
        traverse(root);
        return longestUnivalue - 1;
    }

    public int traverse(TreeNode node) {
        if (node == null) return 0;
        int left = traverse(node.left);
        int right = traverse(node.right);
        return updateLongestUnivalue(node, left, right);
    }

    private int updateLongestUnivalue(TreeNode node, int left, int right) {
        if (node.left != null && node.val == node.left.val && node.right != null && node.val == node.right.val) {
            longestUnivalue = Math.max(longestUnivalue, left + right + 1);
            return Math.max(left, right) + 1;
        }

        if (node.left != null && node.val == node.left.val) {
            longestUnivalue = Math.max(longestUnivalue, left + 1);
            return left + 1;
        }

        if (node.right != null && node.val == node.right.val) {
            longestUnivalue = Math.max(longestUnivalue, right + 1);
            return right + 1;
        }

        return 1;
    }
}
