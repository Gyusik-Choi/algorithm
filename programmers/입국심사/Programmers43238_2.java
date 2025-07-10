package com.example;

import java.util.Arrays;

public class Programmers43238_2 {
    public long solution(int n, int[] times) {
        long low = 1;
        // (long) 으로 캐스팅 하지 않으면 오버플로우가 발생해서 오답이 나오는 테스트케이스가 있다
        long high = (long) Arrays.stream(times).max().getAsInt() * n;
        long answer = 0;
        while (low < high) {
            long mid = low + (high - low) / 2;
            long tempAnswer = 0;
            for (long time : times) {
                tempAnswer += mid / time;
            }
            if (tempAnswer >= n) {
                answer = mid;
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return answer;
    }
}
