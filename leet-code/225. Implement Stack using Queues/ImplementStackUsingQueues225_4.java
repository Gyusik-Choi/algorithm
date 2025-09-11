package com.example;

import java.util.ArrayDeque;
import java.util.Deque;

public class ImplementStackUsingQueues225_4 {
    private final Deque<Integer> queue = new ArrayDeque<>();
    private final Deque<Integer> internalQueue = new ArrayDeque<>();

    public ImplementStackUsingQueues225_4() {}

    public void push(int x) {
        queue.add(x);
    }

    public int pop() {
        // 큐가 빌 때까지 꺼내면서
        while (queue.size() > 1) {
            internalQueue.add(queue.remove());
        }
        int item = queue.remove();
        while (!internalQueue.isEmpty()) {
            queue.add(internalQueue.remove());
        }
        return item;
    }

    public int top() {
        int topItem = pop();
        queue.add(topItem);
        return topItem;
    }

    public boolean empty() {
        return queue.isEmpty();
    }
}
