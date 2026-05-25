package com.example;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class SerializeAndDeserializeBinaryTree297_3 {
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) {
            return "null";
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        StringBuilder sb = new StringBuilder("0");
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node == null) {
                sb.append(",").append("null");
            } else {
                sb.append(",").append(node.val);
                queue.add(node.left);
                queue.add(node.right);
            }
        }
        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        List<String> list = Arrays.stream(data.split(",")).toList();
        if (list.size() == 1) {
            return null;
        }
        int idx = 1;
        TreeNode root = new TreeNode(0);
        root.right = new TreeNode(Integer.parseInt(list.get(idx)));
        TreeNode start = root.right;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(start);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            idx += 1;
            if (!list.get(idx).equals("null")) {
                TreeNode left = new TreeNode(Integer.parseInt(list.get(idx)));
                node.left = left;
                queue.add(left);
            }
            idx += 1;
            if (!list.get(idx).equals("null")) {
                TreeNode right = new TreeNode(Integer.parseInt(list.get(idx)));
                node.right = right;
                queue.add(right);
            }
        }
        return root.right;
    }
}
