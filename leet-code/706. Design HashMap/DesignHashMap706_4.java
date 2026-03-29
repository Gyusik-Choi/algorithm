package com.example;

public class DesignHashMap706_4 {
    private final int SIZE = 1000000;
    private final Node[] nodes = new Node[SIZE];

    public void put(int key, int value) {
        int idx = getIndex(key);
        if (nodes[idx] == null) {
            nodes[idx] = new Node(key, value);
            return;
        }
        Node node = nodes[idx];
        while (node.next != null) {
            if (node.key == key) {
                node.value = value;
                return;
            }
            node = node.next;
        }
        if (node.key == key) {
            node.value = value;
            return;
        }
        node.next = new Node(key, value);
    }

    public int get(int key) {
        int idx = getIndex(key);
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
        int idx = getIndex(key);
        if (nodes[idx] == null) {
            return;
        }
        if (nodes[idx].key == key) {
            if (nodes[idx].next == null) {
                nodes[idx] = null;
            } else {
                nodes[idx] = nodes[idx].next;
            }
            return;
        }
        Node prev = nodes[idx];
        Node node = nodes[idx].next;
        while (node != null) {
            Node next = node.next;
            if (node.key == key) {
                prev.next = next;
                return;
            }
            prev = node;
            node = next;
        }
    }

    private int getIndex(int key) {
        return key % SIZE;
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
