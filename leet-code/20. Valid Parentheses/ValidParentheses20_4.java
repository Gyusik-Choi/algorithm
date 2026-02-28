package com.example;

import java.util.LinkedList;
import java.util.Deque;
import java.util.Map;

public class ValidParentheses20_4 {
    private static final Map<Character, Character> map = Map.of('(', ')', '{', '}', '[', ']');

    public boolean isValid(String s) {
        Deque<Character> stack = new LinkedList<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                if (!map.containsKey(stack.peek())) {
                    return false;
                }
                if (!(map.get(stack.pop()) == c)) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
