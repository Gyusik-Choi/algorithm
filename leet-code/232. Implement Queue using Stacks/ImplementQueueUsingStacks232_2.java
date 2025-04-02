package com.example;

import java.util.ArrayDeque;
import java.util.Deque;

public class ImplementQueueUsingStacks232_2 {

    private final Deque<Integer> stackIn = new ArrayDeque<>();
    private final Deque<Integer> stackOut = new ArrayDeque<>();

    public void push(int x) {
        stackIn.push(x);
    }

    public int pop() {
        while (!stackIn.isEmpty()) {
            stackOut.push(stackIn.pop());
        }
        int item = stackOut.pop();
        while (!stackOut.isEmpty()) {
            stackIn.push(stackOut.pop());
        }
        return item;
    }

    public int peek() {
        while (!stackIn.isEmpty()) {
            stackOut.push(stackIn.pop());
        }
        // 문제의 조건으로 모두 유효한 pop, peek 호출만 발생한다고 해서
        // NullPointerException 에 대한 우려없이 사용함
        int item = stackOut.peek();
        while (!stackOut.isEmpty()) {
            stackIn.push(stackOut.pop());
        }
        return item;
    }

    public boolean empty() {
        return stackIn.isEmpty();
    }
}
