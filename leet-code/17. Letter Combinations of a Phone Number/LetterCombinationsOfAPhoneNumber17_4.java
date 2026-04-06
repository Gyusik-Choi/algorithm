package com.example;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class LetterCombinationsOfAPhoneNumber17_4 {
    private static final Map<Character, List<Character>> phoneMap = Map.ofEntries(
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
        List<String> answer = new ArrayList<>();
        recursion(digits, answer, new StringBuilder());
        return answer;
    }

    private void recursion(String digits, List<String> combinations, StringBuilder combination) {
        if (digits.isEmpty()) {
            combinations.add(combination.toString());
            return;
        }
        // 하나의 재귀 호출에서 digits 의 한 문자만 사용하기 위해
        // digits 를 루프 돌지 않고 digits 의 첫번째 문자만 선택해서
        // 해시맵의 리스트만 루프를 돈다
        for (char ch : phoneMap.get(digits.charAt(0))) {
            combination.append(ch);
            recursion(digits.substring(1), combinations, combination);
            combination.deleteCharAt(combination.length() - 1);
        }
    }
}
