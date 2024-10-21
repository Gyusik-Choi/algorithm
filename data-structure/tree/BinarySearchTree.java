// 구현 진행중
public class BinarySearchTree {
    public Node head;

    public boolean search(int value) {
        return searchTree(head, value);
    }

    private boolean searchTree(Node node, int value) {
        if (node == null) return false;
        if (node.value == value) return true;
        if (node.value > value) return searchTree(node.left, value);
        return searchTree(node.right, value);
    }

    public void add(int value) {
        if (head == null) {
            head = new Node(value);
            return;
        }

        addValue(head, value);
    }

    private void addValue(Node node, int value) {
        if (node.value == value) return;

        if (node.value > value) {
            if (node.left != null) {
                addValue(node.left, value);
            } else {
                node.left = new Node(value);
            }
        } else {
            if (node.right != null) {
                addValue(node.right, value);
            } else {
                node.right = new Node(value);
            }
        }
    }

    public void remove(int value) {

    }

    // 전위, 중위, 후위 순회 메서드 추가

    public static class Node {
        int value;
        Node left;
        Node right;

        Node(int value) {
            this.value = value;
        }
    }
}
