package com.example;

public class MergeTwoSortedLists21_3 {

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) return list2;
        if (list2 == null) return list1;

        if (list1.val <= list2.val) {
            list1.next = mergeTwoLists(list1.next, list2);
        } else {
            ListNode temp = list1;
            list1 = list2;
            list2 = temp;
            list1.next = mergeTwoLists(list1.next, list2);
        }
        return list1;
    }
}
