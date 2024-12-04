package com.example;

import java.util.stream.Collectors;

public class ValidAnagram242 {
    public boolean isAnagram(String s, String t) {
        return isSame(s, t);
    }

    private boolean isSame(String s, String t) {
        // https://www.baeldung.com/java-string-to-stream
        String sortedS = s
                .chars()
                .sorted()
                .mapToObj(c -> (char) c)
                .map(String::valueOf)
                .collect(Collectors.joining());

        String sortedT = t
                .chars()
                .sorted()
                .mapToObj(c -> (char) c)
                .map(String::valueOf)
                .collect(Collectors.joining());

        return sortedS.equals(sortedT);
    }
}
