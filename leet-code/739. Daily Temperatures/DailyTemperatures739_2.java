package com.example;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.List;
import java.util.stream.IntStream;

public class DailyTemperatures739_2 {

    public int[] dailyTemperatures(int[] temperatures) {
        int[] answer = new int[temperatures.length];
        List<Temperature> list = IntStream
                .range(0, temperatures.length)
                .mapToObj(index -> new Temperature(index, temperatures[index]))
                .toList();
        Deque<Temperature> stack = new ArrayDeque<>();
        for (int i = 0; i < list.size(); i++) {
            while (!stack.isEmpty() && stack.peek().temperature < list.get(i).temperature) {
                Temperature prev = stack.pop();
                answer[prev.index] = i - prev.index;
            }
            stack.push(list.get(i));
        }
        return answer;
    }

    private static class Temperature {
        int temperature;
        int index;

        Temperature(int index, int temperature) {
            this.temperature = temperature;
            this.index = index;
        }
    }
}
