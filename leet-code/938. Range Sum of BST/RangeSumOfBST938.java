package com.example;

public class RangeSumOfBST938 {
    private int rangeSum = 0;

    public int rangeSumBST(TreeNode root, int low, int high) {
        if (root == null) return 0;
        if (low <= root.val && root.val <= high) rangeSum += root.val;
        rangeSumBST(root.left, low, high);
        rangeSumBST(root.right, low, high);
        return rangeSum;
    }
}
