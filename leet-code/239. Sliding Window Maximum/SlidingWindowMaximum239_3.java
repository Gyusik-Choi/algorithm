package com.example;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class SlidingWindowMaximum239_3 {
    /**
     * 기존 요소보다 새로 들어오는 요소가 윈도우의 뒤쪽에 있기 때문에
     * 기존 요소보다 새로 들어오는 요소가 큰 경우 기존 요소를 제거해도 된다.
     * 윈도우를 이동하면서 기존 최대값 대신 다른 값을 최대값으로 선택해야 하는데
     * 이때 새 요소가 더 큰 경우 윈도우에 더 오래 있을거라
     * 새 요소보다 작은 기존 요소는 제거해도 무방하다.
     */
    public int[] maxSlidingWindow(int[] nums, int k) {
        List<Integer> answer = new ArrayList<>();
        Deque<int[]> deq = new ArrayDeque<>();
        // 데이터 준비
        for (int i = 0; i < k - 1; i++) {
            evictSmallerFromBack(deq, nums[i]);
            deq.addLast(new int[]{nums[i], i});
        }
        // k - 1 윈도우 크기에서 하나씩 채워서 k 윈도우 크기를 만든다
        for (int i = k - 1; i < nums.length; i++) {
            evictExpiredFromFront(deq, i - k);
            evictSmallerFromBack(deq, nums[i]);
            deq.addLast(new int[]{nums[i], i});
            answer.add(deq.getFirst()[0]);
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }

    /**
     * num 보다 작은 윈도우 요소를 제거한다
     */
    private void evictSmallerFromBack(Deque<int[]> q, int num) {
        while (!q.isEmpty() && q.getLast()[0] < num) {
            q.removeLast();
        }
    }

    /**
     * 윈도우 크기를 벗어난 요소를 앞에서 제거한다
     */
    private void evictExpiredFromFront(Deque<int[]> q, int firstWindow) {
        while (!q.isEmpty() && q.getFirst()[1] <= firstWindow) {
            q.removeFirst();
        }
    }
}
