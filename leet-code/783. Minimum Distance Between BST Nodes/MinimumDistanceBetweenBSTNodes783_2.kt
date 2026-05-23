package com.example

import java.util.*
import kotlin.math.min

class MinimumDistanceBetweenBSTNodes783_2 {
    fun minDiffInBST(root: TreeNode?): Int {
        // 중위순회를 재귀가 아닌 반복으로 구현하되
        // 교재와 달리 왼쪽 자식->부모->오른쪽 자식 순서가 아닌
        // 오른쪽 자식->부모->왼쪽 자식 순서로 탐색
        // 큰 값부터 탐색하면서 Math.abs 를 사용하지 않아도 된다
        var node = root
        var minDiff = 100001
        var prev = 1000000
        val stack = LinkedList<TreeNode>()
        while (!stack.isEmpty() || node != null) {
            while (node != null) {
                stack.push(node)
                node = node?.right
            }
            node = stack.pop()
            minDiff = min(minDiff, prev - node.`val`)
            prev = node.`val`
            node = node.left
        }
        return minDiff
    }
}
