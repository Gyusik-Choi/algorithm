package com.example;

import java.util.ArrayList;
import java.util.List;

public class Permutations46_4 {
    public List<List<Integer>> permute(int[] nums) {
        boolean[] use = new boolean[nums.length];
        List<List<Integer>> answer = new ArrayList<>();
        recursion(nums, use, answer, new ArrayList<>());
        return answer;
    }

    private void recursion(int[] nums, boolean[] used, List<List<Integer>> perms, List<Integer> perm) {
        if (nums.length == perm.size()) {
            perms.add(perm.stream().toList());
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) {
                continue;
            }
            perm.add(nums[i]);
            used[i] = true;
            recursion(nums, used, perms, perm);
            perm.removeLast();
            used[i] = false;
        }
    }
}
