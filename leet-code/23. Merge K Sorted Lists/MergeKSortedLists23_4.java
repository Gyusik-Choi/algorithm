package com.example;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

public class MergeKSortedLists23_4 {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) return null;
        List<ListNode> list = Arrays.stream(lists)
                .filter(Objects::nonNull)
                .collect(Collectors.toList());
        if (list.isEmpty()) return null;
        ListNode root = new ListNode(0);
        mergeKLists(list, root);
        return root.next;
    }

    private void mergeKLists(List<ListNode> list, ListNode node) {
        if (list.isEmpty()) return;
        list.sort(Comparator.comparingInt(n -> n.val));
        ListNode nodeNext = list.removeFirst();
        ListNode next = nodeNext.next;
        nodeNext.next = null;
        node.next = nodeNext;
        if (next != null) {
            list.addFirst(next);
        }
        node = node.next;
        mergeKLists(list, node);
    }
}
