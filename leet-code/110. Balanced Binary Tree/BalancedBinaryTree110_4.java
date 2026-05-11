package com.example;

public class BalancedBinaryTree110_4 {
    private boolean balanced = true;

    // A height-balanced binary tree is a binary tree
    // in which the depth of the two subtrees of every node never differs by more than one.
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        compareDepth(root);
        return balanced;
    }

    private int compareDepth(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int left = compareDepth(node.left);
        int right = compareDepth(node.right);
        if (left == -1 || right == -1) {
            return -1;
        }
        if (Math.abs(left - right) >= 2) {
            balanced = false;
            return -1;
        }
        return Math.max(left, right) + 1;
    }
}
