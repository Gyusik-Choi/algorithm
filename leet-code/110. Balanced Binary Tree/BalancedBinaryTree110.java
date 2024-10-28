package com.example;

public class BalancedBinaryTree110 {
    public boolean isBalanced(TreeNode root) {
        return searchTree(root) != -1;
    }

    private int searchTree(TreeNode node) {
        if (node == null) return 0;
        int left = searchTree(node.left);
        int right = searchTree(node.right);
        if (left == -1 || right == -1) return -1;
        if (Math.abs(left - right) > 1) return -1;
        return Math.max(left, right) + 1;
    }
}
