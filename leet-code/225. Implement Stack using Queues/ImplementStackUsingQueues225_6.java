package com.example;

import java.util.ArrayDeque;
import java.util.Deque;

public class ImplementStackUsingQueues225_6 {
    private final Deque<Integer> q1 = new ArrayDeque<>();
    private final Deque<Integer> q2 = new ArrayDeque<>();

    /**
     * push 에서 stack 구조로 바꿔야
     * top 에서 stack 구조로 바꾸지 않고 바로 조회 가능
     */
    public void push(int x) {
        while (!q1.isEmpty()) {
            q2.add(q1.poll());
        }
        q1.add(x);
        while (!q2.isEmpty()) {
            q1.add(q2.poll());
        }
    }

    public int pop() {
        return q1.poll();
    }

    public int top() {
        return q1.peek();
    }

    public boolean empty() {
        return q1.isEmpty();
    }
}
