package com.example.algorithm;

import java.util.ArrayList;
import java.util.List;

public class Subsets78_3 {
    public List<List<Integer>> subsets(int[] nums) {
        return getPowerSet(nums, 0, new ArrayList<>(), new ArrayList<>());
    }

    private List<List<Integer>> getPowerSet(int[] nums, int idx, List<List<Integer>> powerSet, List<Integer> list) {
        powerSet.add(list.stream().toList());
        if (nums.length == idx) {
            return powerSet;
        }
        for (int i = idx; i < nums.length; i++) {
            list.add(nums[i]);
            getPowerSet(nums, i + 1, powerSet, list);
            list.removeLast();
        }
        return powerSet;
    }
}
