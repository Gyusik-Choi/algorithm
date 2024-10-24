package com.example;

import java.util.ArrayDeque;
import java.util.Deque;

public class SerializeAndDeserializeBinaryTree297 {

    public String serialize(TreeNode root) {
        if (root == null) return "";
        StringBuilder sb = new StringBuilder();
        sb.append(root.val).append(",");
        Deque<TreeNode> deq = new ArrayDeque<>();
        deq.add(root);

        while (!deq.isEmpty()) {
            TreeNode node = deq.poll();
            if (node.left != null) {
                sb.append(node.left.val).append(",");
                deq.add(node.left);
            } else {
                sb.append("#").append(",");
            }

            if (node.right != null) {
                sb.append(node.right.val).append(",");
                deq.add(node.right);
            } else {
                sb.append("#").append(",");
            }
        }

        return sb.toString();
    }

    public TreeNode deserialize(String data) {
        if (data.isEmpty()) return null;
        Deque<TreeNode> deq = new ArrayDeque<>();
        String[] nodeValues = data.split(",");
        TreeNode root = new TreeNode(Integer.parseInt(nodeValues[0]));
        deq.add(root);
        int idx = 0;

        while (!deq.isEmpty()) {
            TreeNode node = deq.poll();
            idx += 1;
            if (!nodeValues[idx].equals("#")) {
                node.left = new TreeNode(Integer.parseInt(nodeValues[idx]));
                deq.add(node.left);
            }

            idx += 1;
            if (!nodeValues[idx].equals("#")) {
                node.right = new TreeNode(Integer.parseInt(nodeValues[idx]));
                deq.add(node.right);
            }
        }
        return root;
    }
}
