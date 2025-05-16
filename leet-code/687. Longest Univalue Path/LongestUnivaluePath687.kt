package com.example

import kotlin.math.max

class LongestUnivaluePath687 {
    private var longestUnivalue = 0

    fun longestUnivaluePath(root: TreeNode?): Int {
        dfs(root)
        val answer = longestUnivalue
        longestUnivalue = 0
        return answer
    }

    private fun dfs(node: TreeNode?): Int {
        if (node == null) {
            return 0
        }

        val left = dfs(node.left)
        val right = dfs(node.right)

        if (isSameWithLeftChild(node) && isSameWithRightChild(node)) {
            // 왼쪽과 오른쪽 자식 노드가 부모 노드로 합쳐지면서 간선이 2개가 늘어난다
            longestUnivalue = max(longestUnivalue, left + right + 2)
            // longestUnivalue 를 구하는 위와 달리 아래는
            // 왼쪽과 오른쪽 간선 중 하나를 정해야 한다
            // 왼쪽, 오른쪽 중 더 길이가 긴 값 + 1
            return max(left, right) + 1
        }

        if (isSameWithLeftChild(node)) {
            longestUnivalue = max(longestUnivalue, left + 1)
            return left + 1
        }

        if (isSameWithRightChild(node)) {
            longestUnivalue = max(longestUnivalue, right + 1)
            return right + 1
        }

        return 0
    }

    private fun isSameWithLeftChild(node: TreeNode?): Boolean {
        return node?.left != null && node.left.`val` == node.`val`
    }

    private fun isSameWithRightChild(node: TreeNode?): Boolean {
        return node?.right != null && node.right.`val` == node.`val`
    }
}
