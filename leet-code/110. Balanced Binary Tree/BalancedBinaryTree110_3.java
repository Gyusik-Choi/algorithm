package com.example.algorithm;

public class BalancedBinaryTree110_3 {
    private boolean balanced = true;

    public boolean isBalanced(TreeNode root) {
        getHeight(root);
        return balanced;
    }

    public int getHeight(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = getHeight(root.left);
        int right = getHeight(root.right);
        if (Math.abs(left - right) > 1) {
            balanced = false;
        }
        return Math.max(left, right) + 1;
    }
}
