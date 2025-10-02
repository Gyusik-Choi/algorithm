package com.example;

import java.util.ArrayList;
import java.util.List;

public class Combinations77_3 {
    private int limit = 0;
    private int size = 0;

    public List<List<Integer>> combine(int n, int k) {
        limit = n;
        size = k;
        return getCombinations(new ArrayList<>(), new ArrayList<>(), 1);
    }

    private List<List<Integer>> getCombinations(List<List<Integer>> combinations, List<Integer> comb, int num) {
        if (comb.size() == size) {
            combinations.add(List.copyOf(comb));
            return combinations;
        }
        for (int i = num; i <= limit; i++) {
            comb.add(i);
            getCombinations(combinations, comb, i + 1);
            comb.remove(comb.size() - 1);
        }
        return combinations;
    }
}
