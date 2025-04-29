package com.example;

import java.util.ArrayList;
import java.util.List;

public class CombinationSum39_2 {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        return getCombinationSum(candidates, target, new ArrayList<>(), new ArrayList<>(), 0);
    }

    private List<List<Integer>> getCombinationSum(int[] candidates,
                                                  int target,
                                                  List<List<Integer>> combinations,
                                                  List<Integer> comb,
                                                  int idx) {
        int sums = getSums(comb);

        if (sums >= target) {
            if (sums == target) {
                combinations.add(comb.stream().toList());
            }
            return combinations;
        }

        for (int i = idx; i < candidates.length; i++) {
            comb.add(candidates[i]);
            getCombinationSum(candidates, target, combinations, comb, i);
            comb.remove(comb.size() - 1);
        }
        return combinations;
    }

    private int getSums(List<Integer> combination) {
        return combination
                .stream()
                .reduce(0, Integer::sum);
    }
}
