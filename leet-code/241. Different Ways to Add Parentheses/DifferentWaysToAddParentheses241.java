package com.example;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class DifferentWaysToAddParentheses241 {

    /**
     * 숫자의 위치는 바뀌지 않는다
     * 연산자의 종류와 위치도 바뀌지 않는다
     * 연산의 순서만 바뀐다
     */
    public List<Integer> diffWaysToCompute(String expression) {
        String[] numbers = expression.split("[-+*]");
        String[] operators = Arrays
                .stream(expression.split("\\d+"))
                .filter(s -> !s.isEmpty()) // [, -, -] 에서 앞의 , 를 제거하기 위함
                .toArray(String[]::new);
        return recursion(numbers, operators, 0, numbers.length - 1);
    }

    private List<Integer> recursion(String[] numbers, String[] operators, int low, int high) {
        if (low == high) return List.of(Integer.parseInt(numbers[low]));
        List<Integer> res = new ArrayList<>();

        for (int mid = low; mid < high; mid++) {
            List<Integer> left = recursion(numbers, operators, low, mid);
            List<Integer> right = recursion(numbers, operators,mid + 1, high);

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
        return res;
    }
}

// 2 * 3 - 4 * 5
// (2 * (3 - (4 * 5))) -> 2 | 3 4 5
// (2 * ((3 - 4) * 5)) -> 2 | 3 4 5
// ((2 * 3) - (4 * 5)) -> 2 3 | 4 5
// (((2 * 3) - 4) * 5) -> 2 3 4 | 5
// ((2 * (3 - 4)) * 5) -> 2 3 4 | 5

