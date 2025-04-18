package com.example;

import java.util.Map;
import java.util.HashMap;

public class JewelsAndStones771_4 {
    public int numJewelsInStones(String jewels, String stones) {
        Map<Character, Integer> stoneMap = new HashMap<>();
        for (char ch : stones.toCharArray()) {
            stoneMap.put(ch, stoneMap.getOrDefault(ch, 0) + 1);
        }
        int count = 0;
        for (char ch : jewels.toCharArray()) {
            if (stoneMap.containsKey(ch)) {
                count += stoneMap.get(ch);
            }
        }
        return count;
    }
}
