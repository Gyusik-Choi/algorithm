package com.example;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;

/**
 * IntervalHeap.java 를 리팩토링
 */
public class IntervalHeap2 {
    private final List<List<Integer>> heap = new ArrayList<>(List.of(List.of(-1, -1)));

    public void add(int num) {
        if (shouldAddNewArray()) {
            heap.add(new ArrayList<>(List.of(num)));
        } else {
            int lastIdx = heap.size() - 1;
            heap.get(lastIdx).add(num);
            // 형제 노드간 비교
            if (isMinGreaterThanMax(lastIdx)) {
                switchElement(lastIdx, 0, lastIdx, 1);
            }
        }
        shiftUp();
    }

    private boolean shouldAddNewArray() {
        return heap.size() == 1 || heap.getLast().size() == 2;
    }

    private void shiftUp() {
        int curIdx = heap.size() - 1;
        while (curIdx > 1) {
            int parentIdx = curIdx / 2;
            int parentFirstElementIdx = 0;
            int parentLastElementIdx = 1;
            int curFirstElementIdx = 0;
            int curLastElementIdx = heap.get(curIdx).size() - 1;
            // 최소힙 수정
            if (heap.get(parentIdx).get(parentFirstElementIdx) > heap.get(curIdx).get(curFirstElementIdx)) {
                switchElement(parentIdx, parentFirstElementIdx, curIdx, curFirstElementIdx);
                curIdx = parentIdx;
                // 최대힙 수정
            } else if (heap.get(parentIdx).get(parentLastElementIdx) < heap.get(curIdx).get(curLastElementIdx)) {
                switchElement(parentIdx, parentLastElementIdx, curIdx, curLastElementIdx);
                curIdx = parentIdx;
            } else {
                break;
            }
        }
    }

    public int pollMin() {
        validateHeap();
        if (containsOnlyRoot()) {
            return extractElement(1, 0);
        }
        int lastIdx = heap.size() - 1;
        switchElement(1, 0, lastIdx, 0);
        int minNumber = extractElement(lastIdx, 0);
        shiftDownMin(1);
        return minNumber;
    }

    public int pollMax() {
        validateHeap();
        if (containsOnlyRoot()) {
            // 루트 리스트 요소의 길이가 1일 수 있어서
            // heap.get(1).size() - 1 로 인덱스 설정
            return extractElement(1, heap.get(1).size() - 1);
        }
        int lastIdx = heap.size() - 1;
        // heap 의 마지막 리스트 요소의 길이가 1일 수 있다
        int lastElementIdx = heap.get(lastIdx).size() - 1;
        switchElement(1, 1, lastIdx, lastElementIdx);
        int maxNumber = extractElement(lastIdx, lastElementIdx);
        shiftDownMax(1);
        return maxNumber;
    }

    private boolean containsOnlyRoot() {
        return heap.size() == 2;
    }

    // 리스트에서 요소를 제거하고 해당 리스트가 비었으면 리스트 자체를 제거
    private int extractElement(int idx, int elementIdx) {
        int element = heap.get(idx).remove(elementIdx);
        removeIfListEmpty(idx);
        return element;
    }

    private void removeIfListEmpty(int idx) {
        if (heap.get(idx).isEmpty()) {
            heap.remove(idx);
        }
    }

    private void shiftDownMin(int idx) {
        int parentIdx = idx;
        int leftChildIdx = parentIdx * 2;
        int rightChildIdx = parentIdx * 2 + 1;
        if (leftChildIdx < heap.size() && heap.get(parentIdx).getFirst() > heap.get(leftChildIdx).getFirst()) {
            parentIdx = leftChildIdx;
        }
        if (rightChildIdx < heap.size() && heap.get(parentIdx).getFirst() > heap.get(rightChildIdx).getFirst()) {
            parentIdx = rightChildIdx;
        }
        if (idx != parentIdx) {
            switchElement(idx, 0, parentIdx, 0);
            // 기존힙과 달리 폐구간 유지를 위해 좌우의 크기를 확인
            if (isMinGreaterThanMax(parentIdx)) {
                switchElement(parentIdx, 0, parentIdx, 1);
            }
            shiftDownMin(parentIdx);
        }
    }

    private void shiftDownMax(int idx) {
        int parentIdx = idx;
        int leftChildIdx = parentIdx * 2;
        int rightChildIdx = parentIdx * 2 + 1;
        if (leftChildIdx < heap.size() && heap.get(parentIdx).getLast() < heap.get(leftChildIdx).getLast()) {
            parentIdx = leftChildIdx;
        }
        if (rightChildIdx < heap.size() && heap.get(parentIdx).getLast() < heap.get(rightChildIdx).getLast()) {
            parentIdx = rightChildIdx;
        }
        if (idx != parentIdx) {
            int lastOfIdx = heap.get(idx).size() - 1;
            int lastOfParentIdx = heap.get(parentIdx).size() - 1;
            switchElement(idx, lastOfIdx, parentIdx, lastOfParentIdx);
            if (isMinGreaterThanMax(parentIdx)) {
                switchElement(parentIdx, 0, parentIdx, 1);
            }
            shiftDownMax(parentIdx);
        }
    }

    public int getMin() {
        validateHeap();
        return heap.get(1).getFirst();
    }

    public int getMax() {
        validateHeap();
        return heap.get(1).getLast();
    }

    private boolean isMinGreaterThanMax(int idx) {
        return heap.get(idx).size() == 2 && heap.get(idx).getFirst() > heap.get(idx).getLast();
    }

    private void switchElement(int idx1, int elementIdx1, int idx2, int elementIdx2) {
        Integer temp = heap.get(idx1).get(elementIdx1);
        heap.get(idx1).set(elementIdx1, heap.get(idx2).get(elementIdx2));
        heap.get(idx2).set(elementIdx2, temp);
    }

    private void validateHeap() {
        if (heap.size() <= 1) {
            throw new NoSuchElementException("heap is empty");
        }
    }
}
