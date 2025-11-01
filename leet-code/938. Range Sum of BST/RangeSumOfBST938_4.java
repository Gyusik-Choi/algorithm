package com.example;

public class RangeSumOfBST938_4 {
    public int rangeSumBST(TreeNode root, int low, int high) {
        if (root == null) {
            return 0;
        }
        int left = rangeSumBST(root.left, low, high);
        int right = rangeSumBST(root.right, low, high);
        return left + right + (low <= root.val && root.val <= high ? root.val : 0);
    }
}
