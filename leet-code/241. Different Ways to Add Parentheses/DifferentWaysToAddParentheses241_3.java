package com.example;

import java.util.*;

public class DifferentWaysToAddParentheses241_3 {
    private final Map<String, List<Integer>> history = new HashMap<>();

    public List<Integer> diffWaysToCompute(String expression) {
        if (history.containsKey(expression)) {
            return history.get(expression);
        }
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < expression.length(); i++) {
            char c = expression.charAt(i);
            if (c == '+' || c == '-' || c == '*') {
                List<Integer> left = diffWaysToCompute(expression.substring(0, i));
                List<Integer> right = diffWaysToCompute(expression.substring(i + 1));

                for (Integer l : left) {
                    for (Integer r : right) {
                        if (c == '+') {
                            result.add(l + r);
                        } else if (c == '-') {
                            result.add(l - r);
                        } else {
                            result.add(l * r);
                        }
                    }
                }
            }
        }
        if (result.isEmpty()) {
            return List.of(Integer.parseInt(expression));
        }
        history.put(expression, result);
        return result;
    }
}


//package com.example;
//
//import java.util.*;
//
//public class DifferentWaysToAddParentheses241_3 {
//    public List<Integer> diffWaysToCompute(String expression) {
//        if (expression.matches("[0-9]+")) {
//            return List.of(Integer.parseInt(expression));
//        }
//        List<Integer> answer = new ArrayList<>();
//        List<Integer> numbers = Arrays.stream(expression.replaceAll("[^0-9]", ",")
//                .split(","))
//                .mapToInt(Integer::parseInt)
//                .boxed()
//                .toList();
//        List<String> operators = Arrays.stream(expression.replaceAll("[0-9]", ",")
//                .split(","))
//                .filter(s -> !s.isEmpty())
//                .toList();
//        addNumbers(numbers, operators, answer, new HashMap<>());
//        return answer;
//    }
//
//    private void addNumbers(List<Integer> nums, List<String> ops, List<Integer> answer, Map<String, Integer> history) {
//        if (nums.size() == 1) {
//            answer.add(nums.getFirst());
//            return;
//        }
////        StringBuilder sb = new StringBuilder();
////        for (int i = 0; i < ops.size(); i++) {
////            sb.append(nums.get(i)).append(ops.get(i));
////        }
////        sb.append(nums.get(ops.size()));
////        if (history.containsKey(sb.toString())) {
////            return;
////        }
////        history.put(sb.toString(), 1);
//        for (int i = 0; i < nums.size() - 1; i++) {
//            int num1 = nums.get(i);
//            String operator = ops.get(i);
//            int num2 = nums.get(i + 1);
//            int result;
//            if (operator.equals("+")) {
//                result = num1 + num2;
//            } else if (operator.equals("-")) {
//                result = num1 - num2;
//            } else {
//                result = num1 * num2;
//            }
//
//            List<Integer> newNums = new ArrayList<>(nums);
//            newNums.add(i, result);
//            newNums.remove(i + 1);
//            newNums.remove(i + 1);
//            List<String> newOps = new ArrayList<>(ops);
//            newOps.remove(i);
//            addNumbers(newNums, newOps, answer, history);
//        }
//    }
//}


//package com.example;
//
//import java.util.ArrayList;
//import java.util.HashMap;
//import java.util.List;
//import java.util.Map;
//
//public class DifferentWaysToAddParentheses241_3 {
//    public List<Integer> diffWaysToCompute(String expression) {
//        if (expression.matches("[0-9]+")) {
//            return List.of(Integer.parseInt(expression));
//        }
//        List<Integer> answer = new ArrayList<>();
//        List<Integer> numbers = new ArrayList<>();
//        List<Character> operators = new ArrayList<>();
//        for (int i = 0; i < expression.length(); i++) {
//            if (i % 2 == 0) {
//                numbers.add(Integer.parseInt(String.valueOf(expression.charAt(i))));
//            } else {
//                operators.add(expression.charAt(i));
//            }
//        }
//        addNumbers(numbers, operators, answer, new HashMap<>());
//        return answer;
//    }
//
//    private void addNumbers(List<Integer> nums, List<Character> ops, List<Integer> answer, Map<Integer, List<String>> history) {
//        if (nums.size() == 1) {
//            answer.add(nums.getFirst());
//            return;
//        }
//        if (nums.size() == 2) {
//            int num1 = nums.getFirst();
//            int num2 = nums.getLast();
//            if (history.containsKey(num1) && history.get(num1).contains(String.valueOf(ops.getFirst() + num2))) {
//                return;
//            }
//            history.put(num1, history.getOrDefault(num1, new ArrayList<>()));
//            history.get(num1).add(String.valueOf(ops.getFirst() + num2));
//        }
//        for (int i = 0; i < nums.size() - 1; i++) {
//            int num1 = nums.get(i);
//            char operator = ops.get(i);
//            int num2 = nums.get(i + 1);
//            int result;
//            if (operator == '+') {
//                result = num1 + num2;
//            } else if (operator == '-') {
//                result = num1 - num2;
//            } else {
//                result = num1 * num2;
//            }
//
//            List<Integer> newNums = new ArrayList<>(nums);
//            newNums.add(i, result);
//            newNums.remove(i + 1);
//            newNums.remove(i + 1);
//            List<Character> newOps = new ArrayList<>(ops);
//            newOps.remove(i);
//            addNumbers(newNums, newOps, answer, history);
//        }
//    }
//}

//package com.example;
//
//import java.util.HashSet;
//import java.util.List;
//
//public class DifferentWaysToAddParentheses241_3 {
//    public List<Integer> diffWaysToCompute(String expression) {
//        HashSet<Integer> set = new HashSet<>();
//        addNumbers(expression, set);
//        return set.stream().toList();
//    }
//
//    private void addNumbers(String expression, HashSet<Integer> set) {
//        if (expression.matches("[0-9]+")) {
//            set.add(Integer.parseInt(expression));
//            return;
//        }
//        for (int i = 0; i < expression.length() - 2; i += 2) {
//            System.out.println("expression -> " + expression);
//            System.out.println("i -> " + i);
//            int num1 = Integer.parseInt(String.valueOf(expression.charAt(i)));
//            System.out.println("num1 -> " + num1);
//            char operator = expression.charAt(i + 1);
//            int num2 = Integer.parseInt(String.valueOf(expression.charAt(i + 2)));
//            System.out.println("num2 -> " + num2);
//            int result;
//            if (operator == '+') {
//                result = num1 + num2;
//            } else if (operator == '-') {
//                result = num1 - num2;
//            } else {
//                result = num1 * num2;
//            }
//
//            if (i == 0) {
//                if (expression.length() > 3) {
//                    addNumbers(result + expression.substring(i + 3), set);
//                } else {
//                    addNumbers(String.valueOf(result), set);
//                }
//            } else if (i == expression.length() - 3) {
//                addNumbers(expression.substring(0, i) + result, set);
//            } else {
//                addNumbers(expression.substring(0, i) + result + expression.substring(i + 3), set);
//            }
//        }
//    }
//}
