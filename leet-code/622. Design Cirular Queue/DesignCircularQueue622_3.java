package com.example;

public class DesignCircularQueue622_3 {

    private int size;
    private int[] circularQueue;
    private int front;
    private int rear;

    public DesignCircularQueue622_3(int k) {
        // 큐의 크기를 k + 1 로 한다
        size = k + 1;
        circularQueue = new int[size];
        for (int i = 0; i < size; i++) {
            circularQueue[i] = -1;
        }
        front = 0;
        rear = 0;
    }

    public boolean enQueue(int value) {
        if (isFull()) {
            return false;
        }
        rear = (rear + 1) % size;
        circularQueue[rear] = value;
        return true;
    }

    public boolean deQueue() {
        if (isEmpty()) {
            return false;
        }
        circularQueue[front] = -1;
        front = (front + 1) % size;
        return true;
    }

    public int Front() {
        if (isEmpty()) {
            return -1;
        }
        return circularQueue[(front + 1) % size];
    }

    public int Rear() {
        if (isEmpty()) {
            return -1;
        }
        return circularQueue[rear];
    }

    public boolean isEmpty() {
        return front == rear;
    }

    public boolean isFull() {
        return (rear + 1) % size == front;
    }
}
