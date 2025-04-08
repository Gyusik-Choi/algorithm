package com.example;

public class CircularQueue {

    private Node head;
    private Node tail;
    private final int maxSize;
    private int size = 0;

    public CircularQueue(int k) {
        maxSize = k;
    }

    public boolean enQueue(int value) {
        if (isFull()) {
            return false;
        }

        if (isEmpty()) {
            head = new Node(value);
            tail = head;
        } else {
            // 기존에 tail 이 참조하던 head 에 대한 참조 제거
            Node oldTail = tail;
            Node newTail = new Node(value);
            oldTail.next = newTail;
            tail = newTail;
            tail.next = head;
        }

        size += 1;
        return true;
    }

    public boolean deQueue() {
        if (isEmpty()) {
            return false;
        }

        if (size == 1) {
            head = null;
            tail = null;
        } else {
            Node newHead = head.next;
            head = newHead;
            tail.next = newHead;
        }

        size -= 1;
        return true;
    }

    public int Front() {
        if (isEmpty()) {
            return -1;
        }
        return head.value;
    }

    public int Rear() {
        if (isEmpty()) {
            return -1;
        }
        return tail.value;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return maxSize == size;
    }

    static class Node {
        int value;
        Node next;

        public Node(int value) {
            this.value = value;
        }
    }
}
