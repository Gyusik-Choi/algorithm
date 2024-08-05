public class MergeTwoSortedLists21 {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) return list2;
        if (list2 == null) return list1;

        // list1 이 기준
        ListNode head;
        if (list1.val > list2.val) {
            ListNode temp = list2;
            list2 = list1;
            list1 = temp;
        }

        head = list1;

        while (list1.next != null && list1.next.val <= list2.val) {
            list1 = list1.next;
        }

        ListNode temp = list1.next;
        list1.next = list2;
        list2 = list2.next;
        list1.next.next = temp;
        list1 = list1.next;

        while (list1 != null && list2 != null) {
            if (list1.next != null && list1.next.val <= list2.val) {
                list1 = list1.next;
                continue;
            }

            ListNode temp1 = list1.next;
            ListNode temp2 = list2;

            while (list2.next != null && list1.next != null && list2.next.val < list1.next.val) {
                list2 = list2.next;
            }

            if (list1.next == null) {
                list1.next = temp2;
                break;
            }

            list1.next = temp2;
            ListNode temp2Next = list2.next;
            list2.next = temp1;
            list2 = temp2Next;
            list1 = temp1;
        }

        return head;
    }
}
