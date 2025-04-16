package com.example;

public class DesignHashMap706_2 {
    /**
     * 문제에서 key, value 범위가 0부터 1000000까지라
     * 서로 다른 키가 동일한 배열 인덱스로 충돌되는 경우는
     * 발생하지 않으나 발생했을 경우를 가정하고 풀이한다
     * 특히 remove 함수의 경우 해당 문제의 조건상
     * 한 인덱스의 Node 가 2개 이상 되는 경우가 없으나
     * 2개 이상이 됐을 경우도 가정하고 풀이한다
     */
    private Node[] nodes = new Node[1000001];

    public void put(int key, int value) {
        int idx = getIdx(key);
        if (nodes[idx] == null) {
            nodes[idx] = new Node(key, value);
            return;
        }

        Node node = nodes[idx];
        // while (node.next != null) {
        // 위의 조건은 안 된다
        // if (node.key == key) 를 만족할 때
        // node.value 를 덮어 써야 하는데
        // while 문이 node.next != null 이면서
        // node.next 가 null 이면 while 문이 종료된다
        // if (node.key == key) 조건을 검사조차 할 수 없다
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
        if (nodes[idx] == null) {
            return -1;
        }

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
        Node prev = null;
        while (node != null) {
            if (node.key == key) {
                // 첫번째 Node 가 일치
                if (prev == null) {
                    nodes[idx] = node.next;
                } else {
                    prev.next = node.next;
                }
                return;
            }
            node = node.next;
            prev = node;
        }
    }

    private int getIdx(int key) {
        return key % nodes.length;
    }

    static class Node {
        int key;
        int value;
        Node next;

        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }
}
