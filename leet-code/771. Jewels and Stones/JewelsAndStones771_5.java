package com.example;

import java.util.HashMap;
import java.util.Map;

public class JewelsAndStones771_5 {
    public int numJewelsInStones(String jewels, String stones) {
        Map<Character, Integer> map = new HashMap<>();
        for (char s : stones.toCharArray()) {
            map.put(s, map.getOrDefault(s, 0) + 1);
        }
        int sums = 0;
        for (char j : jewels.toCharArray()) {
            if (map.containsKey(j)) {
                sums += map.get(j);
            }
        }
        return sums;
    }
}
