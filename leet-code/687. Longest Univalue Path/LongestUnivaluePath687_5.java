package com.example;

public class LongestUnivaluePath687_5 {
    private int maxUnivaluePath = 0;

    public int longestUnivaluePath(TreeNode root) {
        dfs(root);
        return maxUnivaluePath;
    }

    private int dfs(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = dfs(root.left);
        int right = dfs(root.right);

        // maxUnivaluePath 비교
        // 1) left.val, parent.val, right.val 다 같음 -> left + right + 2
        // (단, return 할 때는 left, right 중 하나만 선택할 수 있어서 Math.max(left, right) + 1
        // 2) left.val, parent.val 같음 -> Math.max(left + 1, right)
        // 3) parent.val, right.val 같음 -> Math.max(left, right + 1)
        // 4) left.val, right.val 같음 -> left, right 버린다
        // 5) 다 다름 -> left, right 버린다

        if (root.left != null && root.right != null && root.left.val == root.val && root.val == root.right.val) {
            maxUnivaluePath = Math.max(maxUnivaluePath, left + right + 2);
            return Math.max(left, right) + 1;
        }
        if (root.left != null && root.left.val == root.val) {
            maxUnivaluePath = Math.max(maxUnivaluePath, left + 1);
            return left + 1;
        }
        if (root.right != null && root.val == root.right.val) {
            maxUnivaluePath = Math.max(maxUnivaluePath, right + 1);
            return right + 1;
        }
        return 0;
    }
}
