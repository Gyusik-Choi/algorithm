package com.example;

import java.util.ArrayList;
import java.util.List;

public class CombinationSum39_3 {
    private int[] numbers;
    private int goal;

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        numbers = candidates;
        goal = target;
        return getCombinationSum(new ArrayList<>(), new ArrayList<>(), 0, 0);
    }

    private List<List<Integer>> getCombinationSum(List<List<Integer>> answer,
                                                  List<Integer> combination,
                                                  int sum,
                                                  int idx) {
        if (sum == goal) {
            answer.add(List.copyOf(combination));
            return answer;
        }
        for (int i = idx; i < numbers.length; i++) {
            if (sum + numbers[i] > goal) {
                continue;
            }
            combination.add(numbers[i]);
            sum += numbers[i];
            getCombinationSum(answer, combination, sum, i);
            combination.remove(combination.size() - 1);
            sum -= numbers[i];
        }
        return answer;
    }
}
