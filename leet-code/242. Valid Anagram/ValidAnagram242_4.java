package com.example;

public class ValidAnagram242_4 {
    public boolean isAnagram(String s, String t) {
        int[] sCount = new int[26];
        int[] tCount = new int[26];
        for (char sChar : s.toCharArray()) {
            sCount[sChar - 'a'] += 1;
        }
        for (char tChar : t.toCharArray()) {
            tCount[tChar - 'a'] += 1;
        }
        for (int i = 0; i < 26; i++) {
            if (sCount[i] != tCount[i]) {
                return false;
            }
        }
        return true;
    }
}
