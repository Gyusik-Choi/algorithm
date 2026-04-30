package com.example;

public class MaximumDepthOfBinaryTree104_5 {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftVal = maxDepth(root.left);
        int rightVal = maxDepth(root.right);
        return Math.max(leftVal, rightVal) + 1;
    }
}
