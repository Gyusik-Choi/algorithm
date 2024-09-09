public class DesignHashMap706 {

    // 0 ~ 10^6 사이의 key 가 주어져서
    // 이를 모듈로 연산으로 모두 담을 수 있는 1000001 크기의 배열을 생성
    private final int arraySize = 1000001;
    private Node[] nodes = new Node[arraySize];

    public void put(int key, int value) {
        int idx = getIdx(key);
        if (nodes[idx] == null) {
            nodes[idx] = new Node(key, value);
            return;
        }

        Node node = nodes[idx];
        // while (node.next != null) {
        // 위의 코드를 사용하지 않는 이유는
        // node 의 key 가 파라미터의 key 와 일치하는 경우에도
        // node.next 가 null 이면 해당 while 문을 충족하지 않아서
        // while 문으로 들어오지를 못한다
        // 이를 방지하기 위해 node.next 가 아닌 node 가 null 인지 확인한다
        // 그리고 node 가 null 이 돼서 node.next 에 new Node(key, value) 를 할당할때
        // NullPointerException 이 발생하지 않도록
        // node.next 가 null 이면 node = node.next 를 하지 않고 break 로 종료한다
        while (node != null) {
            if (node.key == key) {
                node.value = value;
                return;
            }

            if (node.next == null) {
                break;
            }
            node = node.next;
        }
        node.next = new Node(key, value);
    }

    public int get(int key) {
        int idx = getIdx(key);
        Node node = nodes[idx];
        while (node != null) {
            if (node.key == key) {
                return node.value;
            }
            node = node.next;
        }
        return -1;
    }

    public void remove(int key) {
        int idx = getIdx(key);
        if (nodes[idx] == null) {
            return;
        }

        Node node = nodes[idx];
        if (node.key == key) {
            if (node.next == null) {
                nodes[idx] = null;
            } else {
                nodes[idx] = node.next;
            }
            return;
        }

        Node prev = node;
        while (node != null) {
            if (node.key == key) {
                prev.next = node.next;
                return;
            }
            prev = node;
            node = node.next;
        }
    }

    private int getIdx(int key) {
        return key % arraySize;
    }

    private static class Node {
        int key;
        int value;
        Node next;

        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }
}
