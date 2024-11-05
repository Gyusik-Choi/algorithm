package com.example;

import java.util.ArrayDeque;
import java.util.Deque;

public class MinimumDistanceBetweenBSTNodes783_2 {
    public int minDiffInBST(TreeNode root) {
        int minDiff = Integer.MAX_VALUE;
        int prev = Integer.MIN_VALUE + 100000;
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode node = root;
        while (!stack.isEmpty() || node != null) {
            while (node != null) {
                stack.push(node);
                node = node.left;
            }
            node = stack.pop();
            minDiff = Math.min(minDiff, Math.abs(prev - node.val));
            prev = node.val;
            node = node.right;
        }
        return minDiff;
    }
}
