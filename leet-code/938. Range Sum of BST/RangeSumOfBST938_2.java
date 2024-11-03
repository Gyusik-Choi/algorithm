package com.example;

public class RangeSumOfBST938_2 {
    public int rangeSumBST(TreeNode root, int low, int high) {
        if (root == null) return 0;
        int rangeSum = 0;
        if (low <= root.val && root.val <= high) rangeSum += root.val;
        rangeSum += rangeSumBST(root.left, low, high);
        rangeSum += rangeSumBST(root.right, low, high);
        return rangeSum;
    }
}
