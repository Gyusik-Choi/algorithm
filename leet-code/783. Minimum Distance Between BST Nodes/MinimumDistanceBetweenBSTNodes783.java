package com.example;

public class MinimumDistanceBetweenBSTNodes783 {
    private int minDiff = Integer.MAX_VALUE;

    // TreeNode 최대값이 100000 이라 오버플로우 방지
    private int prev = Integer.MIN_VALUE + 100000;

    public int minDiffInBST(TreeNode root) {
        if (root == null) return 0;
        minDiffInBST(root.left);
        minDiff = Math.min(minDiff, Math.abs(prev - root.val));
        prev = root.val;
        minDiffInBST(root.right);
        return minDiff;
    }
}
