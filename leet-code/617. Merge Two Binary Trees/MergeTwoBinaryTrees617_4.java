package com.example;

public class MergeTwoBinaryTrees617_4 {
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        // left, right 각각 재귀 호출
        // 재귀 호출 과정에서
        // root1, root2 둘 중 하나가 null 이면 null 아닌 노드 반환하고 바로 종료
        // root1, root2 둘 다 null 이 아니면 추가 탐색
        if (root1 == null) {
            return root2;
        }
        if (root2 == null) {
            return root1;
        }
        TreeNode node = new TreeNode(root1.val + root2.val);
        node.left = mergeTrees(root1.left, root2.left);
        node.right = mergeTrees(root1.right, root2.right);
        return node;
    }
}
