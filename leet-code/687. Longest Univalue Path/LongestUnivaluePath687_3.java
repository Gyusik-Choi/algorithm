public class LongestUnivaluePath687_3 {
    private int longest = 0;

    public int longestUnivaluePath(TreeNode root) {
        dfs(root);
        return longest;
    }

    private int dfs(TreeNode node) {
        if (node == null) return 0;
        int left = dfs(node.left);
        int right = dfs(node.right);

        if (node.left != null && node.left.val == node.val) {
            left += 1;
        } else {
            left = 0;
        }

        if (node.right != null && node.right.val == node.val) {
            right += 1;
        } else {
            right = 0;
        }

        longest = Math.max(longest, left + right);
        return Math.max(left, right);
    }
}
