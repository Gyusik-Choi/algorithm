package com.example;

import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

public class RemoveDuplicateLetters316_3 {
    public String removeDuplicateLetters(String s) {
        Map<Character, Integer> map = new HashMap<>();
        for (char c : s.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        Map<Character, Integer> stackCount = new HashMap<>();

        Deque<Character> stack = new LinkedList<>();
        for (char c : s.toCharArray()) {
            map.put(c, map.get(c) - 1);
            // 이미 스택에 있는 문자는 넣지 않는다
            // 스택에 있는 요소를 빼는 작업 이전에 이를 검증해서
            // s 가 abacb 면서 ab 가 스택에 있고 c 가 a 인 경우
            // b 가 스택에서 꺼내지지 않도록 한다
            if (stackCount.getOrDefault(c, 0) > 0) {
                continue;
            }
            // 스택 최상단의 요소가 c 보다 크고
            // 스택 최상단의 요소가 현재 c 이후에 (for 문의 요소로) 나올 수 있으면
            // 스택에서 제거한다
            while (!stack.isEmpty() && stack.peek() > c && map.get(stack.peek()) > 0) {
                char item = stack.pop();
                stackCount.put(item, stackCount.get(item) - 1);
            }
            stack.push(c);
            stackCount.put(c, 1);
        }

        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        return sb.reverse().toString();
    }
}
