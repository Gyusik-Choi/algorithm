package com.example;

public class MergeTwoBinaryTrees617_3 {
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if (root1 == null) {
            return root2;
        }
        if (root2 == null) {
            return root1;
        }
        // root1, root2 둘 다 null 이 아닌 경우
        TreeNode left = mergeTrees(root1.left, root2.left);
        TreeNode right = mergeTrees(root1.right, root2.right);
        root1.left = left;
        root1.right = right;
        root1.val += root2.val;
        return root1;
    }
}
