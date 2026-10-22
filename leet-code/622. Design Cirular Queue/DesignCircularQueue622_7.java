package com.example;

public class DesignCircularQueue622_7 {
    private final int[] arr;
    private int front = 0;
    private int rear = 0;

    public DesignCircularQueue622_7(int k) {
        // 크기를 1만큼 더 잡아서 한 칸을 빈칸으로 둔다.
        // 그렇게 해야 front, rear 가 같을때
        // 큐가 비었는지 찼는지 구분 못하는 상황이 발생하지 않는다.
        // 예를 들어,
        // k 만큼 배열 크기를 잡게되면 길이가 3인 배열에
        // [1, 2, 3] 와 같이 원소 3개를 순차적으로 넣었다고 가정하겠다.
        // 이때 front 와 rear 가 모두 0이다.
        // 그러면 실제로는 큐가 다 찼으나
        // front 와 rear 가 같아서 isEmpty() 가 true 가 된다.
        arr = new int[k + 1];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = -1;
        }
    }

    public boolean enQueue(int value) {
        if (isFull()) {
            return false;
        }
        arr[rear] = value;
        rear = (rear + 1) % arr.length;
        return true;
    }

    public boolean deQueue() {
        if (isEmpty()) {
            return false;
        }
        arr[front] = -1;
        front = (front + 1) % arr.length;
        return true;
    }

    public int Front() {
        return isEmpty() ? -1 : arr[front];
    }

    public int Rear() {
        if (isEmpty()) {
            return -1;
        }
        // int idx = rear == 0 ? arr.length - 1 : rear - 1;
        // 위는 rear 가 0인지 여부를 구분해서 계산하지만
        // 아래의 방식으로 구분 없이 계산할 수 있음
        return arr[(rear - 1 + arr.length) % arr.length];
    }

    public boolean isEmpty() {
        return front == rear;
    }

    public boolean isFull() {
        return front == (rear + 1) % arr.length;
    }
}
