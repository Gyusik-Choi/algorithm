package com.example;

import java.util.Deque;
import java.util.LinkedList;

public class DailyTemperatures739_3 {
    public int[] dailyTemperatures(int[] temperatures) {
        // [온도, 인덱스]
        Deque<int[]> stack = new LinkedList<>();
        int[] answer = new int[temperatures.length];
        for (int i = 0; i < temperatures.length; i++) {
            while (!stack.isEmpty() && stack.peek()[0] < temperatures[i]) {
                int[] item = stack.pop();
                answer[item[1]] = i - item[1];
            }
            stack.push(new int[]{temperatures[i], i});
        }
        return answer;
    }
}
