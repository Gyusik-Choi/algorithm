package com.example;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class LetterCombinationsOfAPhoneNumber17_5 {
    private static final Map<Character, List<String>> map = Map.of(
            '2', List.of("a", "b", "c"),
            '3', List.of("d", "e", "f"),
            '4', List.of("g", "h", "i"),
            '5', List.of("j", "k", "l"),
            '6', List.of("m", "n", "o"),
            '7', List.of("p", "q", "r", "s"),
            '8', List.of("t", "u", "v"),
            '9', List.of("w", "x", "y", "z"));

    public List<String> letterCombinations(String digits) {
        return traverse(digits, 0, new ArrayList<>(), new StringBuilder());
    }

    private List<String> traverse(String digits, int idx, List<String> list, StringBuilder comb) {
        if (digits.length() == idx) {
            list.add(comb.toString());
            return list;
        }
        for (String alpha : map.get(digits.charAt(idx))) {
            comb.append(alpha);
            traverse(digits, idx + 1, list, comb);
            comb.deleteCharAt(comb.length() - 1);
        }
        return list;
    }
}
