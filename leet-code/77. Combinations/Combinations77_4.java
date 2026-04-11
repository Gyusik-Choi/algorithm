package com.example;

import java.util.ArrayList;
import java.util.List;

public class Combinations77_4 {
    public List<List<Integer>> combine(int n, int k) {
        return recursion(new ArrayList<>(), new ArrayList<>(), 1, n, k);
    }

    private List<List<Integer>> recursion(List<List<Integer>> combs, List<Integer> comb, int num, int numLimit, int sizeLimit) {
        if (comb.size() == sizeLimit) {
            combs.add(comb.stream().toList());
            return combs;
        }
        for (int i = num; i <= numLimit; i++) {
            comb.add(i);
            recursion(combs, comb, i + 1, numLimit, sizeLimit);
            comb.removeLast();
        }
        return combs;
    }
}
