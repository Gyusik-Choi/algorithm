package com.example;

public class DesignCircularDeque641_2 {

    private final int maxSize;
    private int size = 0;
    Node head;
    Node tail;

    public DesignCircularDeque641_2(int k) {
        maxSize = k;
    }

    public boolean insertFront(int value) {
        if (isFull()) {
            return false;
        }

        if (isEmpty()) {
            insertWhenIsEmpty(value);
        } else {
            Node oldHead = head;
            head = new Node(value);
            head.next = oldHead;
            oldHead.prev = head;
        }

        size += 1;
        return true;
    }

    public boolean insertLast(int value) {
        if (isFull()) {
            return false;
        }

        if (isEmpty()) {
            insertWhenIsEmpty(value);
        } else {
            Node oldTail = tail;
            tail = new Node(value);
            tail.prev = oldTail;
            oldTail.next = tail;
        }

        size += 1;
        return true;
    }

    private void insertWhenIsEmpty(int value) {
        head = new Node(value);
        tail = head;
    }

    public boolean deleteFront() {
        if (isEmpty()) {
            return false;
        }

        if (size == 1) {
            deleteWhenIsSizeOne();
        } else {
            Node oldHead = head;
            head = head.next;
            head.prev = null;
            oldHead.next = null;
        }

        size -= 1;
        return true;
    }

    public boolean deleteLast() {
        if (isEmpty()) {
            return false;
        }

        if (size == 1) {
            deleteWhenIsSizeOne();
        } else {
            Node oldTail = tail;
            tail = tail.prev;
            tail.next = null;
            oldTail.prev = null;
        }

        size -= 1;
        return true;
    }

    private void deleteWhenIsSizeOne() {
        head = null;
        tail = null;
    }

    public int getFront() {
        if (isEmpty()) {
            return -1;
        }
        return head.value;
    }

    public int getRear() {
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

    private static class Node {
        int value;
        Node prev;
        Node next;

        Node(int value) {
            this.value = value;
        }
    }
}
