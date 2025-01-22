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

        // mid < high 에 주의
        // numbers 에 비해 operators 는 길이가 항상 1이 짧다
        // numbers 의 시작 인덱스, 마지막 인덱스로 최초의 low, high 를 설정하기 때문에
        // operators 의 마지막 인덱스는 numbers 의 마지막 인덱스보다 항상 1이 짧다
        // 만약에 mid < high 가 아닌 mid <= high 로 하면 무한루프에 빠져 stackoverflow 가 된다
        // 예를 들어,
        // low 가 1, high 가 2라고 가정하면
        // for 문을 시작해서
        // mid 는 1이 됐을 때
        // 첫번째 recursion 호출의 경우 low 와 mid 가 모두 1이라
        // low == high 조건에 걸려서 바로 리턴된다
        // 두번째 recursion 호출의 경우 mid + 1 과 high 모두가 2라
        // low == high 조건에 걸려서 바로 리턴된다
        // mid 가 2가 됐을 때
        // 첫번째 recursion 호출의 경우 low 는 1, mid 는 2라
        // 이때부터 무한루프가 시작된다
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

