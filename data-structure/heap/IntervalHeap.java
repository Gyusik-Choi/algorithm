package com.example;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;

/**
 * 힙의 경우 노드 내부에 값이 하나고
 * 최소힙은 부모 노드가 자식 노드보다 작은게 보장이 되지만
 * 자식 노드간의 크기는 왼쪽, 오른쪽 중 어디가 더 작은지 정해져있지 않다
 * 최대힙은 부모 노드가 자식 노드보다 큰게 보장이 되지만
 * 자식 노드간의 크기는 왼쪽, 오른쪽 중 어디가 더 큰지 정해져있지 않다
 * <br>
 * 인터벌 힙의 경우 노드 내부에 값이 두개고
 * 노드 내부의 왼쪽, 오른쪽 중에 오른쪽이 크거나 같은게 보장된다
 * 그리고 부모 노드와 자식 노드의 경우
 * 최소힙 정보를 다루는 0번 인덱스의 경우 기존 최소힙과 마찬가지로
 * 부모 노드가 자식 노드보다 작은게 보장이 되지만
 * 자식 노드간의 크기는 왼쪽, 오른쪽 중 어디가 더 작은지 정해져있지 않다
 * 최대힙 정보를 다루는 1번 인덱스의 경우 기존 최대힙과 마찬가지로
 * 최대힙은 부모 노드가 자식 노드보다 큰게 보장이 되지만
 * 자식 노드간의 크기는 왼쪽, 오른쪽 중 어디가 더 큰지 정해져있지 않다
 * <br>
 * <a href="https://blog.naver.com/mario002/221978255957">참고 링크</a>
 */
public class IntervalHeap {
    private final List<List<Integer>> heap = new ArrayList<>(List.of(List.of(-1, -1)));

    public void add(int num) {
        if (heap.size() <= 1 || heap.getLast().size() == 2) {
            heap.add(new ArrayList<>(List.of(num)));
        } else {
            heap.getLast().add(num);
            // 형제 노드간 비교
            if (heap.getLast().getFirst() > heap.getLast().getLast()) {
                Integer temp = heap.getLast().getFirst();
                heap.getLast().set(0, heap.getLast().getLast());
                heap.getLast().set(1, temp);
            }
        }
        shiftUp();
    }

    private void shiftUp() {
        int curIdx = heap.size() - 1;
        while (curIdx > 1) {
            int curFirstIdx = 0;
            int curLastIdx = heap.get(curIdx).size() - 1;
            int parentIdx = curIdx / 2;
            // 최소힙 수정
            if (heap.get(parentIdx).getFirst() > heap.get(curIdx).get(curFirstIdx)) {
                int temp = heap.get(parentIdx).getFirst();
                heap.get(parentIdx).set(0, heap.get(curIdx).get(curFirstIdx));
                heap.get(curIdx).set(curFirstIdx, temp);
                curIdx = parentIdx;
                // 최대힙 수정
            } else if (heap.get(parentIdx).getLast() < heap.get(curIdx).getLast()) {
                int temp = heap.get(parentIdx).getLast();
                heap.get(parentIdx).set(1, heap.get(curIdx).getLast());
                heap.get(curIdx).set(curLastIdx, temp);
                curIdx = parentIdx;
            } else {
                break;
            }
        }
    }

    public int pollMin() {
        validateHeap();
        if (heap.size() == 2) {
            // add(5) 후 상태:
            // heap = [[-1,-1], [5]]   heap.size() = 2
            // pollMin() 호출 (원소 1개):
            // heap.size() == 2 → true → heap.get(1).removeFirst() = 5 반환
            // 반환 후 heap.get(1) = [] (빈 리스트, 하지만 제거 안 됨)
            // heap = [[-1,-1], []]   heap.size() = 2 여전히
            // 위의 문제가 발생할 수 있어서 1번 인덱스의 리스트가 비었는지 확인
            int num = heap.get(1).removeFirst();
            if (heap.get(1).isEmpty()) {
                heap.remove(1);
            }
            return num;
        }
        int rootMin = heap.get(1).getFirst();
        int lastIdx = heap.size() - 1;
        int lastNumber = heap.get(lastIdx).removeFirst();
        if (heap.get(lastIdx).isEmpty()) {
            heap.remove(lastIdx);
        }
        heap.get(1).set(0, lastNumber);
        shiftDownMin(1);
        return rootMin;
    }

    public int pollMax() {
        validateHeap();
        if (heap.size() == 2) {
            int num = heap.get(1).removeLast();
            // 1번 인덱스의 리스트가 비었는지 확인
            if (heap.get(1).isEmpty()) {
                heap.remove(1);
            }
            return num;
        }
        int rootMax = heap.get(1).getLast();
        int lastIdx = heap.size() - 1;
        int lastNumber = heap.get(lastIdx).removeLast();
        if (heap.get(lastIdx).isEmpty()) {
            heap.remove(lastIdx);
        }
        heap.get(1).set(1, lastNumber);
        shiftDownMax(1);
        return rootMax;
    }

    private void validateHeap() {
        if (heap.size() <= 1) {
            throw new NoSuchElementException("heap is empty");
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
            int temp = heap.get(idx).getFirst();
            heap.get(idx).set(0, heap.get(parentIdx).getFirst());
            heap.get(parentIdx).set(0, temp);
            // 기존힙과 달리 폐구간 유지를 위해 좌우의 크기를 확인
            if (heap.get(parentIdx).size() == 2 && heap.get(parentIdx).getFirst() > heap.get(parentIdx).getLast()) {
                int temp2 = heap.get(parentIdx).getFirst();
                heap.get(parentIdx).set(0, heap.get(parentIdx).getLast());
                heap.get(parentIdx).set(1, temp2);
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
            int temp = heap.get(idx).get(lastOfIdx);
            heap.get(idx).set(lastOfIdx, heap.get(parentIdx).get(lastOfParentIdx));
            heap.get(parentIdx).set(lastOfParentIdx, temp);
            if (heap.get(parentIdx).size() == 2 && heap.get(parentIdx).getFirst() > heap.get(parentIdx).getLast()) {
                int temp2 = heap.get(parentIdx).getFirst();
                heap.get(parentIdx).set(0, heap.get(parentIdx).getLast());
                heap.get(parentIdx).set(1, temp2);
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
}
