package com.example;

import java.util.*;

public class DifferentWaysToAddParentheses241_2 {

    private String[] numbers;

    private String[] operators;

    private final Map<String, List<Integer>> memo = new HashMap<>();

    public List<Integer> diffWaysToCompute(String expression) {
        numbers = expression.split("[-+*]");
        operators = Arrays
                .stream(expression.split("\\d+"))
                .filter(s -> !s.isEmpty()) // [, -, -] 에서 앞의 , 를 제거하기 위함
                .toArray(String[]::new);
        return recursion(0, numbers.length - 1);
    }

    private List<Integer> recursion(int low, int high) {
        if (low == high) return List.of(Integer.parseInt(numbers[low]));

        String memoKey = Arrays.stream(numbers, low, high).toString();
        if (memo.containsKey(memoKey)) return memo.get(memoKey);

        List<Integer> res = new ArrayList<>();
        for (int mid = low; mid < high; mid++) {
            List<Integer> left = recursion(low, mid);
            List<Integer> right = recursion(mid + 1, high);

            for (Integer l : left) {
                for (Integer r : right) {
                    if (operators[mid].equals("+")) {
                        res.add(l + r);
                    } else if (operators[mid].equals("-")) {
                        res.add(l - r);
                    } else {
                        res.add(l * r);
                    }
                }
            }
        }
        memo.put(memoKey, res);
        return res;
    }
}
