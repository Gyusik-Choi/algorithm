package com.example;

public class DesignCircularDeque641_3 {

    private final int maxSize;
    private int size = 0;
    Node head;
    Node tail;

    public DesignCircularDeque641_3(int k) {
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

        Node node = new Node(value);
        Node oldHead = head.next;
        oldHead.prev = node;
        head.next = node;
        node.prev = head;
        node.next = oldHead;

        size += 1;
        return true;
    }

    public boolean insertLast(int value) {
        if (isFull()) {
            return false;
        }

        Node node = new Node(value);
        Node oldTail = tail.prev;
        oldTail.next = node;
        tail.prev = node;
        node.prev = oldTail;
        node.next = tail;

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

        Node headNext = head.next.next;
        Node deleteNode = head.next;
        head.next = headNext;
        headNext.prev = head;
        deleteNode.prev = null;
        deleteNode.next = null;

        size -= 1;
        return true;
    }

    public boolean deleteLast() {
        if (isEmpty()) {
            return false;
        }

        Node tailPrev = tail.prev.prev;
        Node deleteNode = tail.prev;
        tail.prev = tailPrev;
        tailPrev.next = tail;
        deleteNode.prev = null;
        deleteNode.next = null;

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
        return head.next.value;
    }

    public int getRear() {
        if (isEmpty()) {
            return -1;
        }
        return tail.prev.value;
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
