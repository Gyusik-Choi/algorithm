package com.example;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class ImplementStackUsingQueues225_5 {
    private Deque<Integer> queue = new ArrayDeque<>();

    public void push(int x) {
        List<Integer> temp = new ArrayList<>();
        while (!queue.isEmpty()) {
            temp.add(queue.poll());
        }
        queue.add(x);
        queue.addAll(temp);
    }

    public int pop() {
        return queue.poll();
    }

    public int top() {
        return queue.peek();
    }

    public boolean empty() {
        return queue.size() < 1;
    }
}
