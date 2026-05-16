package com.example;

public class BinarySearchTreeToGreaterSumTree1038_3 {
    private int sums = 0;

    public TreeNode bstToGst(TreeNode root) {
        if (root == null) {
            return null;
        }
        bstToGst(root.right);
        root.val += sums;
        sums = root.val;
        bstToGst(root.left);
        return root;
    }
}
