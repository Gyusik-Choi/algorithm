package com.example.algorithm;

public class MinimumDistanceBetweenBSTNodes783_3 {
    private int previous = -1;

    private int minDiff = Integer.MAX_VALUE;

    public int minDiffInBST(TreeNode root) {
        dfs(root);
        return minDiff;
    }

    private void dfs(TreeNode root) {
        if (root == null) {
            return;
        }

        minDiffInBST(root.left);
        if (previous != -1) {
            minDiff = Math.min(minDiff, Math.abs(previous - root.val));
        }
        previous = root.val;
        minDiffInBST(root.right);
    }
}
