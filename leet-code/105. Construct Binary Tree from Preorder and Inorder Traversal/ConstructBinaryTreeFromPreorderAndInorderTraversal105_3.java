package com.example;

import java.util.Arrays;
import java.util.stream.IntStream;

public class ConstructBinaryTreeFromPreorderAndInorderTraversal105_3 {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 0) {
            return null;
        }
        int val = preorder[0];
        TreeNode node = new TreeNode(val);
        int idx = getIdx(val, inorder);
        if (idx > 0) {
            node.left = buildTree(
                    Arrays.copyOfRange(preorder, 1, idx + 1),
                    Arrays.copyOfRange(inorder, 0, idx));
        }
        if (idx < inorder.length - 1) {
            node.right = buildTree(
                    Arrays.copyOfRange(preorder, idx + 1, preorder.length),
                    Arrays.copyOfRange(inorder, idx + 1, inorder.length));
        }
        return node;
    }

    private int getIdx(int target, int[] array) {
        return IntStream.range(0, array.length)
                .filter(i -> target == array[i])
                .findFirst()
                .orElse(-1);
    }
}
