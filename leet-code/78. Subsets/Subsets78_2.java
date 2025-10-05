package com.example;

import java.util.List;
import java.util.ArrayList;

public class Subsets78_2 {
    public List<List<Integer>> subsets(int[] nums) {
        return getSubsets(new ArrayList<>(), new ArrayList<>(), nums, 0);
    }

    private List<List<Integer>> getSubsets(List<List<Integer>> answer, List<Integer> subset, int[] nums, int idx) {
        answer.add(List.copyOf(subset));
        for (int i = idx; i < nums.length; i++) {
            subset.add(nums[i]);
            getSubsets(answer, subset, nums, i + 1);
            subset.remove(subset.size() - 1);
        }
        return answer;
    }
}
