package com.example;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LetterCombinationsOfAPhoneNumber17_2 {
    private final Map<String, List<String>> map = new HashMap<>(){{
        put("2", List.of("a", "b", "c"));
        put("3", List.of("d", "e", "f"));
        put("4", List.of("g", "h", "i"));
        put("5", List.of("j", "k", "l"));
        put("6", List.of("m", "n", "o"));
        put("7", List.of("p", "q", "r", "s"));
        put("8", List.of("t", "u", "v"));
        put("9", List.of("w", "x", "y", "z"));
    }};

    public List<String> letterCombinations(String digits) {
        return combinations(digits, new ArrayList<>(), new StringBuilder());
    }

    private List<String> combinations(String digits, List<String> combs, StringBuilder comb) {
        if (digits.isEmpty()) {
            if (!comb.isEmpty()) {
                combs.add(comb.toString());
            }
            return combs;
        }

        String digit = digits.substring(0, 1);
        for (String value : map.get(digit)) {
//            comb.append(value);
//            combinations(digits.substring(1), combs, comb);
//            comb.deleteCharAt(comb.length() - 1);
//            위의 코드를 아래처럼 한줄로 구현할 수 있다
            combinations(digits.substring(1), combs, new StringBuilder(comb).append(value));
        }
        return combs;
    }
}
