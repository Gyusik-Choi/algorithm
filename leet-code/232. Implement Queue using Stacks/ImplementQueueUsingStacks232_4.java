package com.example;

import java.util.Deque;
import java.util.LinkedList;

public class ImplementQueueUsingStacks232_4 {
    private final Deque<Integer> stack1 = new LinkedList<>();
    private final Deque<Integer> stack2 = new LinkedList<>();

    public void push(int x) {
        while (!stack1.isEmpty()) {
            stack2.push(stack1.pop());
        }
        stack1.push(x);
        while (!stack2.isEmpty()) {
            stack1.push(stack2.pop());
        }
    }

    public int pop() {
        return stack1.pop();
    }

    public int peek() {
        return stack1.peek();
    }

    public boolean empty() {
        return stack1.isEmpty();
    }
}
