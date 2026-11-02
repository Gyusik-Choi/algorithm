package com.example;

public class JewelsAndStones771_7 {
    public int numJewelsInStones(String jewels, String stones) {
        int[] count = new int[123];
        for (char j : jewels.toCharArray()) count[j] += 1;
        int cnt = 0;
        for (char s : stones.toCharArray()) if (count[s] > 0) cnt += 1;
        return cnt;
    }
}
