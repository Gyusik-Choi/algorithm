package com.example;

/**
 * 이중 연결리스트로 구현
 */
public class DesignCircularDeque641_7 {
    private Node head = null;
    private Node tail = null;
    private int curSize = 0;
    private final int maxSize;

    public DesignCircularDeque641_7(int k) {
        maxSize = k;
    }

    public boolean insertFront(int value) {
        if (isFull()) {
            return false;
        }
        Node node = new Node(value);
        if (isEmpty()) {
            head = node;
            tail = node;
        } else {
            Node oldHead = head;
            head = node;
            oldHead.prev = head;
            head.next = oldHead;
        }
        curSize += 1;
        return true;
    }

    public boolean insertLast(int value) {
        if (isFull()) {
            return false;
        }
        Node node = new Node(value);
        if (isEmpty()) {
            head = node;
            tail = node;
        } else {
            Node oldTail = tail;
            tail = node;
            oldTail.next = tail;
            tail.prev = oldTail;
        }
        curSize += 1;
        return true;
    }

    public boolean deleteFront() {
        if (isEmpty()) {
            return false;
        }
        if (curSize == 1) {
            head = null;
            tail = null;
        } else {
            head = head.next;
            head.prev = null;
        }
        curSize -= 1;
        return true;
    }

    public boolean deleteLast() {
        if (isEmpty()) {
            return false;
        }
        if (curSize == 1) {
            head = null;
            tail = null;
        } else {
            tail = tail.prev;
            tail.next = null;
        }
        curSize -= 1;
        return true;
    }

    public int getFront() {
        return isEmpty() ? -1 : head.value;
    }

    public int getRear() {
        return isEmpty() ? -1 : tail.value;
    }

    public boolean isEmpty() {
        return curSize == 0;
    }

    public boolean isFull() {
        return curSize == maxSize;
    }

    private class Node {
        Node prev;
        Node next;
        int value;

        Node(int value) {
            this.value = value;
        }
    }
}
