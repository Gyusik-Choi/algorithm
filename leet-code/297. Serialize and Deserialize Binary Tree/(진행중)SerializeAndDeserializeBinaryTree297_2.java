package com.example;

import java.util.LinkedList;
import java.util.Queue;

public class SerializeAndDeserializeBinaryTree297_2 {
    // -1000 <= Node.val <= 1000
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) {
            return "";
        }
        StringBuilder sb = new StringBuilder();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node != null) {
                sb.append(node.val).append("/");
                queue.add(node.left);
                queue.add(node.right);
            } else {
                sb.append(-1001).append("/");
            }
        }
        if (!sb.isEmpty()) {
            // 마지막 "-" 제거
            sb.deleteCharAt(sb.length() - 1);
        }
        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.isEmpty()) {
            return null;
        }
        TreeNode root = new TreeNode();
        TreeNode head = root;
        String[] split = data.split("/");
        head.val = Integer.parseInt(split[0]);
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(1, head));
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            for (int i = 0; i < 2; i++) {
                if (i % 2 == 0 && node.idx * 2 - 1<= split.length - 1 && !split[node.idx * 2 - 1].equals("-1001") ) {
                    node.tree.left = new TreeNode(Integer.parseInt(split[node.idx * 2 - 1]));
                    queue.add(new Node(node.idx * 2, node.tree.left));
                    continue;
                }
                if (i % 2 == 1 && node.idx * 2 <= split.length - 1 && !split[node.idx * 2].equals("-1001")) {
                    node.tree.right = new TreeNode(Integer.parseInt(split[node.idx * 2]));
                    queue.add(new Node(node.idx * 2 + 1, node.tree.right));
                }
            }
        }
        return root;
    }

    private static class Node {
        int idx;
        TreeNode tree;

        Node(int idx, TreeNode node) {
            this.idx = idx;
            this.tree = node;
        }
    }
}
