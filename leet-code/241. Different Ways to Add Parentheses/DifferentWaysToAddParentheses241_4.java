package com.example;

import java.util.ArrayList;
import java.util.List;

public class DifferentWaysToAddParentheses241_4 {
    public List<Integer> diffWaysToCompute(String expression) {
        return diffWaysToCompute(expression, new ArrayList<>());
    }

    private List<Integer> diffWaysToCompute(String expression, List<Integer> sums) {
        if (expression.replaceAll("[^0-9]", "").equals(expression)) {
            return new ArrayList<>(List.of(Integer.parseInt(expression)));
        }
        for (int i = 0; i < expression.length(); i++) {
            if (expression.charAt(i) == '+' || expression.charAt(i) == '-' || expression.charAt(i) == '*') {
                List<Integer> left = diffWaysToCompute(expression.substring(0, i), new ArrayList<>());
                List<Integer> right = diffWaysToCompute(expression.substring(i + 1), new ArrayList<>());
                if (expression.charAt(i) == '+') {
                    for (int j = 0; j < left.size(); j++) {
                        for (int k = 0; k < right.size(); k++) {
                            sums.add(left.get(j) + right.get(k));
                        }
                    }
                } else if (expression.charAt(i) == '-') {
                    for (int j = 0; j < left.size(); j++) {
                        for (int k = 0; k < right.size(); k++) {
                            sums.add(left.get(j) - right.get(k));
                        }
                    }
                } else {
                    for (int j = 0; j < left.size(); j++) {
                        for (int k = 0; k < right.size(); k++) {
                            sums.add(left.get(j) * right.get(k));
                        }
                    }
                }
            }
        }
        return sums;
    }
}
