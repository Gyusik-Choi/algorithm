package com.example;

import java.util.HashSet;
import java.util.Set;

public class LongestSubstringWithoutRepeatingCharacters3_6 {
    public int lengthOfLongestSubstring(String s) {
        int longest = 0;
        int left = 0;
        Set<Character> set = new HashSet<>();
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            while (set.contains(c)) {
                set.remove(s.charAt(left++));
            }
            set.add(c);
            longest = Math.max(longest, right - left + 1);
        }
        return longest;
    }
}

//package com.example;
//
//import java.util.ArrayDeque;
//import java.util.Deque;
//import java.util.HashSet;
//import java.util.Set;
//
//public class LongestSubstringWithoutRepeatingCharacters3_6 {
//    // abcabcbb -> 3
//    // pwwkew -> 3
//    public int lengthOfLongestSubstring(String s) {
//        int longest = 0;
//        Set<Character> set = new HashSet<>();
//        Deque<Character> deq = new ArrayDeque<>();
//        for (char c : s.toCharArray()) {
//            while (!deq.isEmpty() && set.contains(c)) {
//                set.remove(deq.pollFirst());
//            }
//            set.add(c);
//            deq.add(c);
//            longest = Math.max(longest, deq.size());
//        }
//        return longest;
//    }
//}
