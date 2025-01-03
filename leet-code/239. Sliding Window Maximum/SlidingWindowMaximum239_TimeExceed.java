package com.example;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class SlidingWindowMaximum239_TimeExceed {
    /**
     * [10000, 9999, 9998, ... 2, 1]
     * 위처럼 내림차순으로 정렬된 배열의 경우
     * 매번 deq 의 모든 요소에서 최대값을 찾는 과정을 반복하면서
     * 시간초과가 발생한다
     * 코드 상으로는 아래의 코드가 for loop 마다 실행된다
     * maxNum = deq.peekFirst();
     * for (Integer num : deq) {
     *  if (num > maxNum) {
     *    maxNum = num;
     *  }
     * }
     */
    public int[] maxSlidingWindow(int[] nums, int k) {
        List<Integer> list = new ArrayList<>();
        Deque<Integer> deq = new ArrayDeque<>();
        int maxNum = nums[0];
        for (int i = 0; i < k; i++) {
            if (maxNum < nums[i]) {
                maxNum = nums[i];
            }
            deq.add(nums[i]);
        }
        list.add(maxNum);

        for (int i = k; i < nums.length; i++) {
            deq.add(nums[i]);
            // 데크의 첫번째 값이 최대값인 경우
            if (maxNum == deq.pollFirst()) {
                // 새로운 값이 최대값인 경우
                if (nums[i] > maxNum) {
                    maxNum = nums[i];
                } else {
                    if (deq.isEmpty()) {
                        maxNum = nums[i];
                    } else {
                        maxNum = deq.peekFirst();
                        for (Integer num : deq) {
                            if (num > maxNum) {
                                maxNum = num;
                            }
                        }
                    }
                }
            } else {
                if (nums[i] > maxNum) {
                    maxNum = nums[i];
                }
            }
            list.add(maxNum);
        }

        return list
                .stream()
                .mapToInt(i -> i)
                .toArray();
    }
}
