package com.example;

public class DiameterOfBinaryTree543_3 {
    public int diameterOfBinaryTree(TreeNode root) {
        int[] answer = dfs(root);
        return answer[0];
    }

    // [최대값, 왼쪽과 오른쪽 중 더 큰 값]
    private int[] dfs(TreeNode root) {
        if (root == null) {
            return new int[]{0, 0};
        }

        // 최대값과 왼쪽, 오른쪽 중 더 큰 값을 모두 구해야 한다
        int[] left = dfs(root.left);
        int[] right = dfs(root.right);
        return new int[]{
                Math.max(Math.max(left[0], right[0]), left[1] + right[1]),
                Math.max(left[1], right[1]) + 1
        };
    }
}
