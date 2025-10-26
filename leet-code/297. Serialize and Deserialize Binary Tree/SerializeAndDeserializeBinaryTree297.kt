package com.example.algorithm

class SerializeAndDeserializeBinaryTree297 {
    // Encodes a URL to a shortened URL.
    fun serialize(root: TreeNode?): String {
        if (root == null) {
            return "null,"
        }

        var serialized = ""
        val queue = ArrayDeque<TreeNode?>()
        queue.add(root)
        while (queue.isNotEmpty()) {
            val node = queue.removeFirst()
            if (node == null) {
                serialized += "null,"
            } else {
                serialized += node.`val`.toString() + ","
                queue.add(node.left)
                queue.add(node.right)
            }
        }
        return serialized
    }

    // Decodes your encoded data to tree.
    fun deserialize(data: String): TreeNode? {
        if (data.startsWith("null,")) {
            return null
        }

        val words = data.split(",").filter{ it.isNotEmpty() }
        val root = TreeNode(words[0].toInt())
        val nodeQueue = ArrayDeque<TreeNode>()
        nodeQueue.add(root)

        var idx = 0
        while (nodeQueue.isNotEmpty()) {
            val node = nodeQueue.removeFirst()

            idx += 1
            if (words[idx] != "null") {
                node.left = TreeNode(words[idx].toInt())
                nodeQueue.add(node.left)
            }

            idx += 1
            if (words[idx] != "null") {
                node.right = TreeNode(words[idx].toInt())
                nodeQueue.add(node.right)
            }
        }
        return root
    }
}
