package com.example;

public class DesignCircularDeque641_5 {
    private final Node head = new Node(-1);
    private final Node tail = new Node(-1);
    private final int limit;
    private int size;

    public DesignCircularDeque641_5(int k) {
        head.next = tail;
        tail.prev = head;
        limit = k;
        size = 0;
    }

    public boolean insertFront(int value) {
        if (isFull()) {
            return false;
        }
        Node oldNode = head.next;
        Node newNode = new Node(value);
        head.next = newNode;
        newNode.prev = head;
        newNode.next = oldNode;
        oldNode.prev = newNode;
        size += 1;
        return true;
    }

    public boolean insertLast(int value) {
        if (isFull()) {
            return false;
        }
        Node oldNode = tail.prev;
        Node newNode = new Node(value);
        newNode.prev = oldNode;
        oldNode.next = newNode;
        tail.prev = newNode;
        newNode.next = tail;
        size += 1;
        return true;
    }

    public boolean deleteFront() {
        if (isEmpty()) {
            return false;
        }
        Node newNext = head.next.next;
        Node oldNext = head.next;
        oldNext.prev = null;
        oldNext.next = null;
        head.next = newNext;
        newNext.prev = head;
        size -= 1;
        return true;
    }

    public boolean deleteLast() {
        if (isEmpty()) {
            return false;
        }
        Node newPrev = tail.prev.prev;
        Node oldPrev = tail.prev;
        oldPrev.prev = null;
        oldPrev.next = null;
        tail.prev = newPrev;
        newPrev.next = tail;
        size -= 1;
        return true;
    }

    public int getFront() {
        return isEmpty() ? -1 : head.next.value;
    }

    public int getRear() {
        return isEmpty() ? -1 : tail.prev.value;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == limit;
    }

    private static class Node {
        Node prev;
        Node next;
        int value;

        private Node(int value) {
            this.value = value;
        }
    }
}
