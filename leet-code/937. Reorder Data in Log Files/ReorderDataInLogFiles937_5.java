package com.example.algorithm;

import java.util.ArrayList;
import java.util.List;

public class ReorderDataInLogFiles937_5 {
    public String[] reorderLogFiles(String[] logs) {
        List<String> letterLogs = new ArrayList<>();
        List<String> digitLogs = new ArrayList<>();
        for (String log : logs) {
            if (Character.isAlphabetic(log.split(" ")[1].charAt(0))) {
                letterLogs.add(log);
            } else {
                digitLogs.add(log);
            }
        }
        letterLogs.sort((a, b) -> {
            String[] aLog = a.split(" ", 2);
            String[] bLog = b.split(" ", 2);
            if (aLog[1].compareTo(bLog[1]) == 0) {
                return aLog[0].compareTo(bLog[0]);
            }
            return aLog[1].compareTo(bLog[1]);
        });
        letterLogs.addAll(digitLogs);
        return letterLogs.toArray(new String[0]);
    }
}
