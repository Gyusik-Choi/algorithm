package com.example;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class SlidingWindowMaximum239 {
    public int[] maxSlidingWindow(int[] nums, int k) {
        List<Integer> list = new ArrayList<>();
        Deque<Integer> deq = new ArrayDeque<>();

        for (int i = 0; i < nums.length; i++) {
            // 맨 앞의 요소가 window 범위를 벗어난 경우
            if (!deq.isEmpty() && deq.peek() < i - k + 1) deq.poll();
            // 덱의 맨 앞에 최대값을 유지할 수 있도록
            // nums[i] 보다 작은 요소들이 있다면 뒤에서부터 제거한다
            while (!deq.isEmpty() && nums[deq.peekLast()] < nums[i]) deq.pollLast();
            deq.add(i);
            // 첫번째 k 를 만족하지 못하는 상황이면 최대값을 구하지 않도록 한다
            // k 가 3이라고 할때 i 가 0 혹은 1이면
            // 크기가 아직 3을 채우지 못했기 때문에 최대값을 구하면 안된다
            if (i >= k - 1) list.add(nums[deq.peek()]);
        }

        return list
                .stream()
                .mapToInt(i -> i)
                .toArray();
    }
}
