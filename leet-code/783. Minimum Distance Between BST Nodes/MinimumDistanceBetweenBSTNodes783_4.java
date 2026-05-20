package com.example;

public class MinimumDistanceBetweenBSTNodes783_4 {
    private int minDiff = 100001;
    private int prevValue = Integer.MAX_VALUE;

    public int minDiffInBST(TreeNode root) {
        dfs(root);
        return minDiff;
    }

    public void dfs(TreeNode node) {
        if (node == null) {
            return;
        }
        dfs(node.right);
        minDiff = Math.min(minDiff, prevValue - node.val);
        prevValue = node.val;
        dfs(node.left);
    }
}
