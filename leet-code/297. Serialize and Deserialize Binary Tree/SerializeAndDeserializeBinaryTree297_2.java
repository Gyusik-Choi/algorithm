package com.example;

import java.util.LinkedList;
import java.util.Queue;

public class SerializeAndDeserializeBinaryTree297_2 {
    // -1000 <= Node.val <= 1000
    public String serialize(TreeNode root) {
        if (root == null) {
            return "";
        }

        Queue<TreeNode> queue = new LinkedList<>();
        StringBuilder data = new StringBuilder();
        queue.add(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node != null) {
                data.append(node.val).append(",");
                queue.add(node.left);
                queue.add(node.right);
            } else {
                data.append("-1001").append(",");
            }
        }
        data.deleteCharAt(data.lastIndexOf(","));
        return data.toString();
    }

    public TreeNode deserialize(String data) {
        if (data == null || data.isEmpty()) {
            return null;
        }

        String[] datas = data.split(",");
        TreeNode root = new TreeNode(Integer.parseInt(datas[0]));
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        int idx = 1;
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();

            if (!datas[idx].equals("-1001")) {
                node.left = new TreeNode(Integer.parseInt(datas[idx]));
                queue.add(node.left);
            }

            idx += 1;

            if (!datas[idx].equals("-1001")) {
                node.right = new TreeNode(Integer.parseInt(datas[idx]));
                queue.add(node.right);
            }

            idx += 1;
        }

        return root;
    }
}
