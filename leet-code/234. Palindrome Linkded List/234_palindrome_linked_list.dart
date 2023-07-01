class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);
}

class Solution {
  bool isPalindrome(ListNode? head) {
    // fast 가 첫번째 while 문에서 null 이 될 수 있어서 nullable 로 선언
    ListNode? fast = head!;
    // slow 가 두번째 while 문에서 null 이 될 수 있어서 nullable 로 선언
    ListNode? slow = head;
    // 처음에 null 로 값을 두기 위해 nullable 로 선언
    ListNode? rev = null;

    // ignore: unnecessary_null_comparison
    while (fast != null && fast.next != null) {
      fast = fast.next!.next;
      
      ListNode? tempSlow = slow;
      ListNode? tempRev = rev;
      slow = slow!.next;
      rev = tempSlow;
      rev!.next = tempRev;
    }

    // ignore: unnecessary_null_comparison
    if (fast != null) {
      slow = slow!.next;
    }

    while (slow != null && slow.val == rev!.val) {
      slow = slow.next;
      rev = rev.next;
    }

    return rev == null;
  }
}

void main() {
  ListNode node = ListNode(1);
  node.next = ListNode(2);
  node.next!.next = ListNode(3);
  node.next!.next!.next = ListNode(2);
  node.next!.next!.next!.next = ListNode(1);

  Solution solution = Solution();
  print(solution.isPalindrome(node)); 
}
