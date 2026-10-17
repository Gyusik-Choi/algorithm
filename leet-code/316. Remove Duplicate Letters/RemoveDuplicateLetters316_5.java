package com.example;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

public class RemoveDuplicateLetters316_5 {
    public String removeDuplicateLetters(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Integer> stackCounter = new HashMap<>();
        Map<Character, Integer> counter = new HashMap<>();
        for (char c : s.toCharArray()) counter.put(c, counter.getOrDefault(c, 0) + 1);
        for (char c : s.toCharArray()) {
            counter.put(c, counter.getOrDefault(c, 0) - 1);
            if (stackCounter.getOrDefault(c, 0) > 0) continue;
            while (!stack.isEmpty() && stack.peek() > c && counter.getOrDefault(stack.peek(), 0) > 0) {
                Character character = stack.pop();
                stackCounter.put(character, stackCounter.get(character) - 1);
            }
            stack.push(c);
            stackCounter.put(c, stackCounter.getOrDefault(c, 0) + 1);
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) sb.insert(0, stack.pop());
        return sb.toString();
    }
}
