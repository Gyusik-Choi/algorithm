public class DesignCircularDeque641 {
    private final int maxSize;
    private int length = 0;
    private final DoublyLinkedList head;
    private final DoublyLinkedList tail;

    public DesignCircularDeque641(int k) {
        maxSize = k;
        head = new DoublyLinkedList(-1);
        tail = new DoublyLinkedList(-1);
        head.right = tail;
        tail.left = head;
    }

    public boolean insertFront(int value) {
        if (isFull()) {
            return false;
        }
        DoublyLinkedList node = new DoublyLinkedList(value);
        node.left = head;
        node.right = head.right;
        // node 는 left, right 로 방금 연결이 되었으나
        // head, head.right 는 node 와 아직 연결되지 않아서
        // 기존의 연결을 유지하고 있는 상태다
        // 여기서 node 와 연결하면서 head, head.right 의 연결이 바뀐다
        //
        // node 를 먼저 head, head.right 와 연결했기 때문에
        // head, head.right 의 연결 상태가 바뀌지 않아서
        // head.right 의 참조값을 유지하기 위해 별도의 변수로 선언하지 않아도 됐다
        head.right.left = node;
        head.right = node;
        length++;
        return true;
    }

    public boolean insertLast(int value) {
        if (isFull()) {
            return false;
        }
        DoublyLinkedList node = new DoublyLinkedList(value);
        node.right = tail;
        node.left = tail.left;
        tail.left.right = node;
        tail.left = node;
        length++;
        return true;
    }

    public boolean deleteFront() {
        if (isEmpty()) {
            return false;
        }
        DoublyLinkedList node = head.right;
        head.right = head.right.right;
        head.right.left = head;
        node.left = null;
        node.right = null;
        length--;
        return true;
    }

    public boolean deleteLast() {
        if (isEmpty()) {
            return false;
        }
        DoublyLinkedList node = tail.left;
        tail.left = tail.left.left;
        tail.left.right = tail;
        node.left = null;
        node.right = null;
        length--;
        return true;
    }

    public int getFront() {
        return isEmpty() ? -1 : head.right.value;
    }

    public int getRear() {
        return isEmpty() ? -1 : tail.left.value;
    }

    public boolean isEmpty() {
        return length == 0;
    }

    public boolean isFull() {
        return maxSize == length;
    }

    static class DoublyLinkedList {
        int value;
        DoublyLinkedList left;
        DoublyLinkedList right;

        DoublyLinkedList(int value) {
            this.value = value;
        }
    }
}
