package com.example;

public class LongestUnivaluePath687_4 {
    private int longestUnivalue = 0;

    public int longestUnivaluePath(TreeNode root) {
        dfs(root);
        return longestUnivalue;
    }

    private int dfs(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = dfs(root.left);
        int right = dfs(root.right);
        if (root.left != null && root.left.val == root.val && root.right != null && root.right.val == root.val) {
            longestUnivalue = Math.max(left + right + 2, longestUnivalue);
            return Math.max(left, right) + 1;
        }
        if (root.left != null && root.left.val == root.val) {
            longestUnivalue = Math.max(left + 1, longestUnivalue);
            return left + 1;
        }
        if (root.right != null && root.right.val == root.val) {
            longestUnivalue = Math.max(right + 1, longestUnivalue);
            return right + 1;
        }
        return 0;
    }
}
