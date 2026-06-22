package com.example;

import java.util.stream.Collectors;

public class ValidAnagram242_5 {
    public boolean isAnagram(String s, String t) {
        return s.chars()
                .sorted()
                .mapToObj(Integer::toString)
                .collect(Collectors.joining())
                .equals(t.chars()
                        .sorted()
                        .mapToObj(Integer::toString)
                        .collect(Collectors.joining()));
    }
}
