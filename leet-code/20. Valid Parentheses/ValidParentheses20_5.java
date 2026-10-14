package com.example.algorithm;

import java.util.Deque;
import java.util.LinkedList;
import java.util.Map;

public class ValidParentheses20_5 {
    private static final Map<Character, Character> PAIRS = Map.of('(', ')', '{', '}', '[', ']');

    public boolean isValid(String s) {
        Deque<Character> stack = new LinkedList<>();
        for (char c : s.toCharArray()) {
            if (PAIRS.containsKey(c)) {
                stack.push(c);
            } else {
                if (stack.isEmpty() || !PAIRS.get(stack.peek()).equals(c)) {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.isEmpty();
    }
}
