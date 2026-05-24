package com.example;

import java.util.ArrayDeque;
import java.util.Deque;

public class MinimumAbsoluteDifferenceInBST530_2 {
    public int getMinimumDifference(TreeNode root) {
        int minDiff = 100001;
        int prevVal = 1000000;
        Deque<TreeNode> stack = new ArrayDeque<>();
        while (!stack.isEmpty() || root != null) {
            while (root != null) {
                stack.push(root);
                root = root.right;
            }
            root = stack.pop();
            minDiff = Math.min(minDiff, prevVal - root.val);
            prevVal = root.val;
            root = root.left;
        }
        return minDiff;
    }
}
