package com.example;

public class DiameterOfBinaryTree543_3 {
    private int maxDiameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        traverse(root);
        return maxDiameter;
    }

    private int traverse(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = traverse(root.left);
        int right = traverse(root.right);
        maxDiameter = Math.max(maxDiameter, left + right);
        return Math.max(left, right) + 1;
    }
}
