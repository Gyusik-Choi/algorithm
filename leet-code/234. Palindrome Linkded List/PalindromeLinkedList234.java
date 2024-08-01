import java.util.*;


public class PalindromeLinkedList234 {
    public boolean isPalindrome(ListNode head) {
        List<Integer> nums = new ArrayList<>();
        while (head != null) {
            nums.add(head.val);
            head = head.next;
        }

        List<Integer> reversedNums = new ArrayList<>(nums);
        Collections.reverse(reversedNums);

        for (int i = 0; i < nums.size(); i++) {
            if (!Objects.equals(nums.get(i), reversedNums.get(i))) {
                return false;
            }
        }

        return true;
    }
}
