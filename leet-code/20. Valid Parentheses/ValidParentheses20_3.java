package com.example;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Map;

public class ValidParentheses20_3 {
    private static final Map<Character, Character> parentheses = Map.of(
            '(', ')',
            '{', '}',
            '[', ']'
    );

    public boolean isValid(String s) {
        Deque<Character> queue = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (parentheses.containsKey(c)) {
                queue.push(c);
            } else {
                if (queue.isEmpty()) {
                    return false;
                }
                if (!parentheses.get(queue.peek()).equals(c)) {
                    return false;
                }
                queue.pop();
            }
        }
        return queue.isEmpty();
    }
}
