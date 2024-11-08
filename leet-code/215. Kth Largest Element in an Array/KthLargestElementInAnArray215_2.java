package com.example;

import java.util.*;
import java.util.stream.IntStream;

public class KthLargestElementInAnArray215_2 {
    public int findKthLargest(int[] nums, int k) {
        MaxBinaryHeap queue = new MaxBinaryHeap();
        for (int num : nums) queue.add(num);
        for (int i = 0; i < k - 1; i++) queue.poll();
        return queue.poll();
    }

    private static class MaxBinaryHeap {
        private final List<Integer> list;

        MaxBinaryHeap() {
            // https://codechacha.com/ko/java-collections-arraylist-initialization/
            list = new ArrayList<Integer>(){{ add(null); }};
        }

        public void add(int n) {
            list.add(n);
            shiftUp();
        }

        private void shiftUp() {
            int childIdx = list.size() - 1;
            int parentIdx = childIdx / 2;

            while (parentIdx > 0) {
                if (list.get(parentIdx) < list.get(childIdx)) {
                    swap(parentIdx, childIdx);
                    childIdx = parentIdx;
                    parentIdx = childIdx / 2;
                } else {
                    break;
                }
            }
        }

        public int poll() {
            swap(1, list.size() - 1);
            int pollNum = list.get(list.size() - 1);
            list.remove(list.size() - 1);
            shiftDown(1);
            return pollNum;
        }

        private void shiftDown(int idx) {
            int parentIdx = idx;
            int leftChildIdx = 2 * idx;
            int rightChildIdx = 2 * idx + 1;

            if (leftChildIdx < list.size() && list.get(parentIdx) < list.get(leftChildIdx)) {
                parentIdx = leftChildIdx;
            }

            if (rightChildIdx < list.size() && list.get(parentIdx) < list.get(rightChildIdx)) {
                parentIdx = rightChildIdx;
            }

            if (parentIdx != idx) {
                swap(parentIdx, idx);
                shiftDown(parentIdx);
            }
        }

        private void swap(int parentIdx, int childIdx) {
            int temp = list.get(parentIdx);
            list.set(parentIdx, list.get(childIdx));
            list.set(childIdx, temp);
        }
    }
}
