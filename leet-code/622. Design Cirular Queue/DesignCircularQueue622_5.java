package com.example;

public class DesignCircularQueue622_5 {
    private int[] arr;
    private int size;
    private int start = 0;
    private int end = 0;

    public DesignCircularQueue622_5(int k) {
        arr = new int[k + 1];
        size = k + 1;
        // enQueue 의 입력이 0 이상 1000 이하
        for (int i = 0; i < k + 1; i++) {
            arr[i] = -1;
        }
    }

    public boolean enQueue(int value) {
        if (isFull()) {
            return false;
        }
        end = (end + 1) % size;
        arr[end] = value;
        return true;
    }

    public boolean deQueue() {
        if (isEmpty()) {
            return false;
        }
        start = (start + 1) % size;
        arr[start] = -1;
        return true;
    }

    public int Front() {
        if (isEmpty()) {
            return -1;
        }
        return arr[(start + 1) % size];
    }

    public int Rear() {
        if (isEmpty()) {
            return -1;
        }
        return arr[end];
    }

    public boolean isEmpty() {
        return start == end;
    }

    public boolean isFull() {
        return (end + 1) % size == start;
    }
}
