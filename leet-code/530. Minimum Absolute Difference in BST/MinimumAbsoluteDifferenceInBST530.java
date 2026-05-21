package com.example;

public class MinimumAbsoluteDifferenceInBST530 {
    private int minDiff = 100001;
    private int prevVal = 1000000;

    public int getMinimumDifference(TreeNode root) {
        dfs(root);
        return minDiff;
    }

    private void dfs(TreeNode node) {
        if (node == null) return;
        dfs(node.right);
        minDiff = Math.min(minDiff, prevVal - node.val);
        prevVal = node.val;
        dfs(node.left);
    }
}
