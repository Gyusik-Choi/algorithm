package com.example;

public class DesignCircularDeque641_4 {
    private final Node head;
    private final Node tail;
    private final int maxSize;
    private int curSize = 0;

    public DesignCircularDeque641_4(int k) {
        maxSize = k;
        head = new Node(-1);
        tail = new Node(-1);
        head.next = tail;
        tail.prev = head;
    }

    public boolean insertFront(int value) {
        if (isFull()) {
            return false;
        }
        curSize += 1;
        Node newNode = new Node(value);
        Node nextNode = head.next;
        head.next = newNode;
        newNode.prev = head;
        newNode.next = nextNode;
        nextNode.prev = newNode;
        return true;
    }

    public boolean insertLast(int value) {
        if (isFull()) {
            return false;
        }
        curSize += 1;
        Node newNode = new Node(value);
        Node prevNode = tail.prev;
        tail.prev = newNode;
        newNode.prev = prevNode;
        newNode.next = tail;
        prevNode.next = newNode;
        return true;
    }

    public boolean deleteFront() {
        if (isEmpty()) {
            return false;
        }
        curSize -= 1;
        Node originHeadNext = head.next;
        Node newHeadNext = head.next.next;
        originHeadNext.prev = null;
        originHeadNext.next = null;
        head.next = newHeadNext;
        newHeadNext.prev = head;
        return true;
    }

    public boolean deleteLast() {
        if (isEmpty()) {
            return false;
        }
        curSize -= 1;
        Node originTailPrev = tail.prev;
        Node newTailPrev = tail.prev.prev;
        originTailPrev.prev = null;
        originTailPrev.next = null;
        tail.prev = newTailPrev;
        newTailPrev.next = tail;
        return true;
    }

    public int getFront() {
        return isEmpty() ? -1 : head.next.value;
    }

    public int getRear() {
        return isEmpty() ? -1 : tail.prev.value;
    }

    public boolean isEmpty() {
        return curSize == 0;
    }

    public boolean isFull() {
        return curSize == maxSize;
    }

    static class Node {
        Node prev;
        Node next;
        int value;

        public Node(int value) {
            this.value = value;
        }
    }
}
