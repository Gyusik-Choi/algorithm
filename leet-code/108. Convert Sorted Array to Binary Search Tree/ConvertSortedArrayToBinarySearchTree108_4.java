package com.example;

import java.util.Arrays;

public class ConvertSortedArrayToBinarySearchTree108_4 {
    public TreeNode sortedArrayToBST(int[] nums) {
        // [-10,-3,0,5,9] -> [0,-3,9,-10,null,5] / [0,-10,5,null,-3,null,9]
        // [1,3] -> [1,null,3] / [3,1]
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

//    private TreeNode dfs(int[] nums) {
//        if (nums.length == 0) {
//            return null;
//        }
//        int idx = nums.length / 2;
//        TreeNode node = new TreeNode(nums[idx]);
//        int[] left = idx > 0 ? Arrays.copyOfRange(nums, 0, idx) : new int[]{};
//        int[] right = idx + 1 < nums.length ? Arrays.copyOfRange(nums, idx + 1, nums.length) : new int[]{};
//        node.left = dfs(left);
//        node.right = dfs(right);
//        return node;
//    }
}
