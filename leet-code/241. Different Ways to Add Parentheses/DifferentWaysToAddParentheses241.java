package com.example;

import java.util.ArrayList;
import java.util.List;

public class DifferentWaysToAddParentheses241 {

    /**
     * 숫자의 위치는 바뀌지 않는다
     * 연산자의 종류와 위치도 바뀌지 않는다
     * 연산의 순서만 바뀐다
     */
    public List<Integer> diffWaysToCompute(String expression) {
        return new ArrayList<>();
    }
}

// 2 * 3 - 4 * 5
// (2 * (3 - (4 * 5))) -> 2 | 3 4 5
// (2 * ((3 - 4) * 5)) -> 2 | 3 4 5
// ((2 * 3) - (4 * 5)) -> 2 3 | 4 5
// (((2 * 3) - 4) * 5) -> 2 3 4 | 5
// ((2 * (3 - 4)) * 5) -> 2 3 4 | 5
