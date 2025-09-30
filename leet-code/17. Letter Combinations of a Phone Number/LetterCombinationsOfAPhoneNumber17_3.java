package com.example.algorithm;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class LetterCombinationsOfAPhoneNumber17_3 {
    private static Map<Character, List<Character>> numberMap = Map.ofEntries(
            Map.entry('2', List.of('a', 'b', 'c')),
            Map.entry('3', List.of('d', 'e', 'f')),
            Map.entry('4', List.of('g', 'h', 'i')),
            Map.entry('5', List.of('j', 'k', 'l')),
            Map.entry('6', List.of('m', 'n', 'o')),
            Map.entry('7', List.of('p', 'q', 'r', 's')),
            Map.entry('8', List.of('t', 'u', 'v')),
            Map.entry('9', List.of('w', 'x', 'y', 'z'))
    );

    public List<String> letterCombinations(String digits) {
        return dfs(digits, new ArrayList<>(), "");
    }

    private List<String> dfs(String digits, List<String> combinations, String combination) {
        if (digits.isEmpty()) {
            combinations.add(combination);
            return combinations;
        }
        for (Character c : numberMap.get(digits.charAt(0))) {
            combination = combination + c.toString();
            dfs(digits.substring(1), combinations, combination);
            combination = combination.substring(0, combination.length() - 1);
        }
        return combinations;
    }
}
