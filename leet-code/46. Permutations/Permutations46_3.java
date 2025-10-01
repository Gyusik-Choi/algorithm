package com.example;

import java.util.ArrayList;
import java.util.List;

public class Permutations46_3 {
    public List<List<Integer>> permute(int[] nums) {
        return dfs(nums, new ArrayList<>(), new ArrayList<>());
    }

    private List<List<Integer>> dfs(int[] nums, List<List<Integer>> permutations, List<Integer> permutation) {
        if (nums.length == permutation.size()) {
            permutations.add(List.copyOf(permutation));
            return permutations;
        }
        for (int num : nums) {
            if (!permutation.contains(num)) {
                permutation.add(num);
                dfs(nums, permutations, permutation);
                permutation.remove(permutation.size() - 1);
            }
        }
        return permutations;
    }
}
