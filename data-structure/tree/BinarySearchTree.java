import java.util.ArrayList;
import java.util.List;

public class BinarySearchTree {
    private com.example.BinarySearchTree.Node head;

    public boolean isEmpty() {
        return head == null;
    }

    public boolean search(int value) {
        return searchTree(head, value);
    }

    private boolean searchTree(com.example.BinarySearchTree.Node node, int value) {
        if (node == null) return false;
        if (node.value == value) return true;
        if (node.value > value) return searchTree(node.left, value);
        return searchTree(node.right, value);
    }

    public boolean add(int value) {
        if (isEmpty()) {
            head = new com.example.BinarySearchTree.Node(value);
            return true;
        }
        return addValue(head, value);
    }

    private boolean addValue(com.example.BinarySearchTree.Node node, int value) {
        if (node.value == value) return false;

        if (node.value > value) {
            if (node.left != null) {
                return addValue(node.left, value);
            } else {
                node.left = new com.example.BinarySearchTree.Node(value);
            }
        } else {
            if (node.right != null) {
                return addValue(node.right, value);
            } else {
                node.right = new com.example.BinarySearchTree.Node(value);
            }
        }
        return true;
    }

    public boolean remove(int value) {
        if (isEmpty()) return false;

        if (head.value == value) {
            if (head.left == null && head.right == null) {
                head = null;
            } else if (head.left == null) {
                head = head.right;
            } else if (head.right == null) {
                head = head.left;
            } else {
                com.example.BinarySearchTree.Node rightSmallestNode = findSmallestNodeFromRightChild(head.right);
                head.value = rightSmallestNode.value;
                return removeNode(head, head.right, rightSmallestNode.value);
            }
            return true;
        }
        return head.value > value ? removeNode(head, head.left, value) : removeNode(head, head.right, value);
    }

    private boolean removeNode(com.example.BinarySearchTree.Node parent, com.example.BinarySearchTree.Node cur, int value) {
        if (cur == null) return false;

        if (cur.value == value) {
            if (cur.left == null && cur.right == null) {
                if (parent.left == cur) {
                    parent.left = null;
                } else {
                    parent.right = null;
                }
            } else if (cur.left == null) {
                if (parent.left == cur) {
                    parent.left = cur.right;
                } else {
                    parent.right = cur.right;
                }
            } else if (cur.right == null) {
                if (parent.left == cur) {
                    parent.left = cur.left;
                } else {
                    parent.right = cur.left;
                }
            } else {
                com.example.BinarySearchTree.Node rightSmallestNode = findSmallestNodeFromRightChild(cur.right);
                cur.value = rightSmallestNode.value;
                return removeNode(cur, cur.right, rightSmallestNode.value);
            }
            return true;
        }
        return cur.value > value ? removeNode(cur, cur.left, value) : removeNode(cur, cur.right, value);
    }

    private com.example.BinarySearchTree.Node findSmallestNodeFromRightChild(com.example.BinarySearchTree.Node cur) {
        if (cur.left == null) {
            return cur;
        }
        return findSmallestNodeFromRightChild(cur.left);
    }

    // 전위 순회
    public List<Integer> preOrder() {
        return preOrderTree(new ArrayList<>(), head);
    }

    private List<Integer> preOrderTree(List<Integer> list, com.example.BinarySearchTree.Node node) {
        if (node == null) return list;
        list.add(node.value);
        preOrderTree(list, node.left);
        preOrderTree(list, node.right);
        return list;
    }

    // 중위 순회
    public List<Integer> inOrder() {
        return inOrderTree(new ArrayList<>(), head);
    }

    private List<Integer> inOrderTree(List<Integer> list, com.example.BinarySearchTree.Node node) {
        if (node == null) return list;
        inOrderTree(list, node.left);
        list.add(node.value);
        inOrderTree(list, node.right);
        return list;
    }

    // 후위 순회
    public List<Integer> postOrder() {
        return postOrderTree(new ArrayList<>(), head);
    }

    private List<Integer> postOrderTree(List<Integer> list, com.example.BinarySearchTree.Node node) {
        if (node == null) return list;
        postOrderTree(list, node.left);
        postOrderTree(list, node.right);
        list.add(node.value);
        return list;
    }

    private static class Node {
        int value;
        com.example.BinarySearchTree.Node left;
        com.example.BinarySearchTree.Node right;

        Node(int value) {
            this.value = value;
        }
    }
}
