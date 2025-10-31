package com.example

class BinarySearchTreeToGreaterSumTree1038 {
    // 이진 탐색 트리에서
    // 부모 노드는 직접 연결된 왼쪽, 오른쪽 자식 노드 외에는 직접 접근할 수 없다
    // 그렇지만 이 문제는 연결된 부모 노드 및 자식 노드 외에도
    // 다른 노드의 값을 사용할 수 있어야 한다
    // 직접 접근할 수는 없어서 값을 갱신하고 참조할 수 있는 별도의 변수를 사용한다
    // 예를 들어 부모 노드가 자신의 오른쪽 자식 노드 외에
    // 오른쪽 자식 노드의 왼쪽 자식노드의 값이 필요할 수 있다
    private var toAdd = 0

    fun bstToGst(root: TreeNode?): TreeNode? {
        if (root == null || (root.left == null && root.right == null)) {
            return root
        }
        inorderTraverse(root)
        return root
    }

    fun inorderTraverse(root: TreeNode?) {
        if (root == null) {
            return
        }
        inorderTraverse(root.right)
        root.`val` += toAdd
        toAdd = root.`val`
        inorderTraverse(root.left)
    }
}
