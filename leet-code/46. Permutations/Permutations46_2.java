package com.example;

import java.util.ArrayList;
import java.util.List;

public class Permutations46_2 {
    public List<List<Integer>> permute(int[] nums) {
        return getPermutations(new ArrayList<>(), new ArrayList<>(), nums, new boolean[nums.length]);
    }

    private List<List<Integer>> getPermutations(List<List<Integer>> perms,
                                                List<Integer> perm,
                                                int[] nums,
                                                boolean[] visit) {
        if (perm.size() == nums.length) {
            perms.add(perm.stream().toList());
            return perms;
        }

        for (int i = 0; i < nums.length; i++) {
            if (!visit[i]) {
                visit[i] = true;
                perm.add(nums[i]);
                getPermutations(perms, perm, nums, visit);
                visit[i] = false;
                perm.remove(perm.size() - 1);
            }
        }
        return perms;
    }
}
