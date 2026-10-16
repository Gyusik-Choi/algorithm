package com.example.algorithm;

public class DesignHashMap706_5 {
    private final int DEFAULT_INITIAL_CAPACITY = 1 << 4;
    private final float DEFAULT_LOAD_FACTOR = 0.75f;
    private int capacity;
    private int size;
    private int threshold;
    private Node[] table;

    public DesignHashMap706_5() {
        // 테이블 최대 크기
        capacity = DEFAULT_INITIAL_CAPACITY;
        // 현재 테이블 크기
        size = 0;
        // 다음 리사이즈 기준 원소 개수 (= capacity × loadFactor)
        threshold = (int) (DEFAULT_LOAD_FACTOR * DEFAULT_INITIAL_CAPACITY);
        // 테이블
        table = new Node[capacity];
    }

    public void put(int key, int value) {
        int bucket = getIndex(key);
        if (table[bucket] == null) {
            table[bucket] = new Node(key, value);
            size++;
            if (shouldIncrease()) increase();
        } else {
            Node cur = table[bucket];
            while (cur.next != null) {
                if (cur.key == key) {
                    cur.value = value;
                    return;
                }
                cur = cur.next;
            }
            if (cur.key == key) {
                cur.value = value;
                return;
            }
            cur.next = new Node(key, value);
            size++;
            if (shouldIncrease()) increase();
        }
    }

    private void put(Node[] table, int key, int value) {
        int bucket = getIndex(key);
        if (table[bucket] == null) {
            table[bucket] = new Node(key, value);
        } else {
            Node cur = table[bucket];
            while (cur.next != null) {
                if (cur.key == key) {
                    cur.value = value;
                    return;
                }
                cur = cur.next;
            }
            if (cur.key == key) {
                cur.value = value;
                return;
            }
            cur.next = new Node(key, value);
        }
    }

    private int getIndex(int key) {
        int hash = mixBits(getHashCode(key));
        return hash & (capacity - 1);
    }

    private int getHashCode(int key) {
        return key;
    }

    private int mixBits(int hash) {
        return hash ^ (hash >>> 16);
    }

    public int get(int key) {
        int index = getIndex(key);
        Node node = table[index];
        if (node == null) return -1;
        while (node != null) {
            if (node.key == key) return node.value;
            node = node.next;
        }
        return -1;
    }

    public void remove(int key) {
        int index = getIndex(key);
        Node node = table[index];
        if (node == null) return;
        if (node.key == key) {
            table[index] = node.next;
            size--;
            return;
        }
        Node prev = node;
        node = node.next;
        while (node != null) {
            if (node.key == key) {
                prev.next = node.next;
                node.next = null;
                size--;
                return;
            }
            prev = node;
            node = node.next;
        }
    }

    private boolean shouldIncrease() {
        return size >= threshold;
    }

    private void increase() {
        capacity = capacity << 1;
        threshold = threshold << 1;
        reAllocate();
    }

    private void reAllocate() {
        Node[] newTable = new Node[capacity];
        for (Node value : table) {
            Node node = value;
            while (node != null) {
                put(newTable, node.key, node.value);
                node = node.next;
            }
        }
        table = newTable;
    }

    static class Node {
        private final int key;
        private int value;
        private Node next;

        private Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }
}
