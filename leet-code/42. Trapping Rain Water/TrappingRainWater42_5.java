package com.example;

import java.util.ArrayDeque;
import java.util.Deque;

public class TrappingRainWater42_5 {
    public int trap(int[] height) {
        Deque<Integer> stack = new ArrayDeque<>();
        int sums = 0;
        for (int i = 0; i < height.length; i++) {
            while (!stack.isEmpty() && height[stack.peek()] < height[i]) {
                Integer top = stack.pop();
                if (stack.isEmpty()) {
                    break;
                }
                int high = Math.min(height[stack.peek()], height[i]) - height[top];
                int distance = i - stack.peek() - 1;
                sums += high * distance;
            }
            stack.push(i);
        }
        return sums;
    }
}
