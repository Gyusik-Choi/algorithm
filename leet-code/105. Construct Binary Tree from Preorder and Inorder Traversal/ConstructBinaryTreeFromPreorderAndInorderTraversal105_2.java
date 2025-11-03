package com.example;

import java.util.Arrays;

public class ConstructBinaryTreeFromPreorderAndInorderTraversal105_2 {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 0) {
            return null;
        }
        TreeNode node = new TreeNode(preorder[0]);
        int idx = getIdx(inorder, preorder[0]);
        node.left = buildTree(Arrays.copyOfRange(preorder, 1, idx + 1), Arrays.copyOfRange(inorder, 0, idx));
        node.right = buildTree(Arrays.copyOfRange(preorder, idx + 1, preorder.length), Arrays.copyOfRange(inorder, idx + 1, inorder.length));
        return node;
    }

    private int getIdx(int[] array, int target) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == target) {
                return i;
            }
        }
        return -1;
    }
}
