package com.example;

import java.util.ArrayList;
import java.util.List;

public class CombinationSum39_4 {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        return recursion(new ArrayList<>(), new ArrayList<>(), candidates, target, 0);
    }

    private List<List<Integer>> recursion(List<List<Integer>> combs, List<Integer> comb, int[] nums, int target, int idx) {
        int sums = getSum(comb);
        for (int i = idx; i < nums.length; i++) {
            int num = nums[i];
            if (sums + num == target) {
                comb.add(num);
                combs.add(comb.stream().toList());
                comb.removeLast();
            } else if (sums + num < target) {
                comb.add(num);
                recursion(combs, comb, nums, target, i);
                comb.removeLast();
            }
        }
        return combs;
    }

    private int getSum(List<Integer> comb) {
        return comb.stream().reduce(0, Integer::sum);
    }
}
