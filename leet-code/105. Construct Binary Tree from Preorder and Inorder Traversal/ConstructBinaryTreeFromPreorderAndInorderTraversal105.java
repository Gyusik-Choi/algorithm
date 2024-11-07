package com.example;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.List;
import java.util.stream.IntStream;

public class ConstructBinaryTreeFromPreorderAndInorderTraversal105 {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return createTree(arraytoDeque(preorder), arrayToList(inorder));
    }

    private TreeNode createTree(Deque<Integer> preorder, List<Integer> inorder) {
        if (inorder.isEmpty()) return null;
        int value = preorder.poll();
        int inIdx = inorder.indexOf(value);
        TreeNode root = new TreeNode(value);
        root.left = createTree(preorder, sliceList(inorder, 0, inIdx));
        root.right = createTree(preorder, sliceList(inorder, inIdx + 1, inorder.size()));
        return root;
    }

    private Deque<Integer> arraytoDeque(int[] arr) {
        Deque<Integer> deq = new ArrayDeque<>();
        for (int num : arr) deq.add(num);
        return deq;
    }

    private List<Integer> arrayToList(int[] arr) {
        // https://stackoverflow.com/questions/27522741/incompatible-types-inference-variable-t-has-incompatible-bounds
        return IntStream.of(arr).boxed().toList();
    }

    private List<Integer> sliceList(List<Integer> list, int start, int end) {
        return list.stream().skip(start).limit(end).toList();
    }
}
