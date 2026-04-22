package com.example;

import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

public class SmallestSubsequenceOfDistinctCharacters1081 {
    public String smallestSubsequence(String s) {
        Map<Character, Integer> counter = new HashMap<>();
        Map<Character, Boolean> existsInStack = new HashMap<>();
        Deque<Character> stack = new LinkedList<>();
        for (char c : s.toCharArray()) {
            counter.putIfAbsent(c, 0);
            counter.put(c, counter.get(c) + 1);
            existsInStack.put(c, false);
        }
        for (char c : s.toCharArray()) {
            counter.put(c, counter.get(c) - 1);
            if (existsInStack.get(c)) {
                continue;
            }
            while (!stack.isEmpty() && counter.get(stack.peek()) > 0 && stack.peek() > c) {
                existsInStack.put(stack.pop(), false);
            }
            stack.push(c);
            existsInStack.put(c, true);
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        return sb.reverse().toString();
    }
}
