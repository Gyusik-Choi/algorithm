package com.example;

public class DesignCircularQueue622_6 {
    private Node front = null;
    private Node rear = null;
    private int curSize = 0;
    private final int maxSize;

    public DesignCircularQueue622_6(int k) {
        maxSize = k;
    }

    public boolean enQueue(int value) {
        if (isFull()) {
            return false;
        }
        if (isEmpty()) {
            front = new Node(value);
            rear = front;
        } else {
            Node oldRear = rear;
            rear = new Node(value);
            oldRear.next = rear;
        }
        curSize += 1;
        return true;
    }

    public boolean deQueue() {
        if (isEmpty()) {
            return false;
        }
        // front 와 rear.next 의 참조를 변경해야 한다
        Node next = front.next;
        front = next;
        rear.next = next;
        curSize -= 1;
        return true;
    }

    public int Front() {
        return isEmpty() ? -1 : front.value;
    }

    public int Rear() {
        return isEmpty() ? -1 : rear.value;
    }

    public boolean isEmpty() {
        return curSize == 0;
    }

    public boolean isFull() {
        return curSize == maxSize;
    }

    private class Node {
        final int value;
        Node next;

        Node(int value) {
            this.value = value;
        }
    }
}
