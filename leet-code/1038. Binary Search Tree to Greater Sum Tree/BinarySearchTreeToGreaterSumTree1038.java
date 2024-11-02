package com.example;

public class BinarySearchTreeToGreaterSumTree1038 {
    private int acc = 0;

    public TreeNode bstToGst(TreeNode root) {
        if (root == null) return null;
        bstToGst(root.right);
        root.val += acc;
        acc = root.val;
        bstToGst(root.left);
        return root;
    }
}
