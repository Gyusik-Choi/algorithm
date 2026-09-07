package com.example;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class ReorderDataInLogFiles937_6 {
    public String[] reorderLogFiles(String[] logs) {
        List<String> letters = Arrays.stream(logs)
                .filter(log -> Character.isAlphabetic(log.split(" ")[1].charAt(0)))
                .sorted((log1, log2) -> {
                    String[] a = log1.split(" ", 2);
                    String[] b = log2.split(" ", 2);
                    return a[1].equals(b[1]) ? a[0].compareTo(b[0]) : a[1].compareTo(b[1]);
                })
                .toList();
        List<String> digits = Arrays.stream(logs)
                .filter(log -> !Character.isAlphabetic(log.split(" ")[1].charAt(0)))
                .toList();
        List<String> answer = new ArrayList<>();
        answer.addAll(letters);
        answer.addAll(digits);
        return answer.toArray(String[]::new);
    }
}
