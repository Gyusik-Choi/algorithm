package com.example;

public class RangeSumOfBST938_5 {
    public int rangeSumBST(TreeNode root, int low, int high) {
        if (root == null) {
            return 0;
        }
        int leftSums = root.val <= low ? 0 : rangeSumBST(root.left, low, high);
        int rightSums = root.val >= high ? 0 : rangeSumBST(root.right, low, high);
        return leftSums + rightSums + (low <= root.val && root.val <= high ? root.val : 0);
    }
}
