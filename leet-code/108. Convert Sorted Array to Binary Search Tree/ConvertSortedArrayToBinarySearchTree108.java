package com.example;

import java.util.List;
import java.util.stream.IntStream;

public class ConvertSortedArrayToBinarySearchTree108 {
    public TreeNode sortedArrayToBST(int[] nums) {
        return createBST(IntStream.of(nums).boxed().toList());
    }

    private TreeNode createBST(List<Integer> list) {
        if (list.isEmpty()) return null;
        int center = (list.size() - 1) / 2;
        TreeNode node = new TreeNode(list.get(center));
        TreeNode leftChild = createBST(sliceList(list, 0, center));
        TreeNode rightChild = createBST(sliceList(list, center + 1, list.size() - center + 1));
        node.left = leftChild;
        node.right = rightChild;
        return node;
    }

    private List<Integer> sliceList(List<Integer> list, int skipNum, int limitNum) {
        return list.stream().skip(skipNum).limit(limitNum).toList();
    }
}
