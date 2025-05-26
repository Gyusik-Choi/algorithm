package com.example;

public class BinarySearchTreeToGreaterSumTree1038_2 {
    // 트리 순회
    // 오른쪽 -> 부모 -> 왼쪽
    public TreeNode bstToGst(TreeNode root) {
        if (root == null) {
            return new TreeNode(0);
        }

        bstToGst(root.right);
        root.val += sum;
        sum = root.val;
        bstToGst(root.left);
        return root;
    }

    private int sum = 0;
}
