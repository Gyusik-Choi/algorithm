package com.example;

public class DesignHashMap706_3 {
    private final int totalSize = 1000000;
    private Node[] arr = new Node[totalSize];

    public DesignHashMap706_3() {}

    public void put(int key, int value) {
        int idx = getKeyIndex(key);
        if (arr[idx] == null) {
            arr[idx] = new Node(key, value);
        } else {
            Node node = arr[idx];
            if (node.key == key) {
                node.value = value;
                return;
            }
            while (node.next != null) {
                if (node.key == key) {
                    node.value = value;
                    return;
                }
                node = node.next;
            }
            node.next = new Node(key, value);
        }
    }

    public int get(int key) {
        int idx = getKeyIndex(key);
        if (arr[idx] == null) {
            return -1;
        }
        Node node = arr[idx];
        while (node != null) {
            if (node.key == key) {
                return node.value;
            }
            node = node.next;
        }
        return -1;
    }

    public void remove(int key) {
        int idx = getKeyIndex(key);
        if (arr[idx] == null) {
            return;
        }
        if (arr[idx].key == key) {
            arr[idx] = arr[idx].next;
            return;
        }
        Node prev = arr[idx];
        Node node = arr[idx].next;
        while (node != null) {
            if (node.key == key) {
                prev.next = node.next;
                return;
            }
            prev = node;
            node = node.next;
        }
    }

    private int getKeyIndex(int key) {
        return key % totalSize;
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
