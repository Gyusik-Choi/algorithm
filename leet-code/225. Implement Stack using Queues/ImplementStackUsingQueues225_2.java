public class ImplementStackUsingQueues225_2 {
    // head 에 임의의 노드 할당
    // 실제 연결 리스트는 head 이후의 노드
    Node head = new Node(0);

    public ImplementStackUsingQueues225_2() {}

    // 연결 리스트 맨 뒤에 삽입
    public void push(int x) {
        Node node = head;
        while (node.next != null) {
            node = node.next;
        }
        node.next = new Node(x);
    }

    // 연결 리스트 맨 뒤를 제거
    public int pop() {
        Node node = head;
        while (node.next.next != null) {
            node = node.next;
        }
        int popNumber = node.next.val;
        node.next = null;
        return popNumber;
    }

    // 연결 리스트 맨 뒤의 값 리턴
    public int top() {
        Node node = head;
        while (node.next != null) {
            node = node.next;
        }
        return node.val;
    }

    public boolean empty() {
        return head.next == null;
    }

    public int size() {
        int num = 0;
        Node node = head;
        while (node != null) {
            num += 1;
            node = node.next;
        }
        return num;
    }

    private class Node {
        int val;
        Node next;

        public Node(int val) {
            this.val = val;
        }
    }
}

