package com.example;

import java.util.Arrays;

public class ConvertSortedArrayToBinarySearchTree108_4 {
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length == 0) {
            return null;
        }
        int idx = nums.length / 2;
        TreeNode node = new TreeNode(nums[idx]);
        int[] left = idx > 0 ? Arrays.copyOfRange(nums, 0, idx) : new int[]{};
        int[] right = idx + 1 < nums.length ? Arrays.copyOfRange(nums, idx + 1, nums.length) : new int[]{};
        node.left = sortedArrayToBST(left);
        node.right = sortedArrayToBST(right);
        return node;
    }
}
