package com.example;

import java.util.HashMap;
import java.util.Map;

public class MinimumWindowSubstring76 {
    public String minWindow(String s, String t) {
        Map<Character, Integer> need = new HashMap<>();
        for (char c : t.toCharArray()) need.put(c, need.getOrDefault(c, 0) + 1);
        int missing = t.length();
        int minLength = Integer.MAX_VALUE;
        int left = 0, right = 0, start = 0, end = 0;

        for (char c : s.toCharArray()) {
            right += 1;
            if (need.containsKey(c) && need.get(c) > 0) missing -= 1;
            // need 에 없는 문자는 음수가 된다
            need.put(c, need.getOrDefault(c, 0) - 1);

            // missing 이 0이면 찾는 문자를 다 찾은 경우라
            // if 문 아래의 로직을 실행한다
            if (missing > 0) continue;

            // left 가 t 에 해당하지 않는 문자를 가리키고 있다면
            // left 를 이동해서 window 의 크기를 줄인다
            while (left < right && need.get(s.charAt(left)) < 0) {
                need.put(s.charAt(left), need.getOrDefault(s.charAt(left), 0) + 1);
                left += 1;
            }

            // minLength 를 갱신할 수 있는 경우
            // minLength, start, end 를 갱신한다
            if (minLength > right - left + 1) {
                minLength = right - left + 1;
                start = left;
                end = right;
            }

            // 추가적으로 minLength 를 갱신할 기회를 찾기 위해 left 를 한칸 이동한다
            // 다음 for loop 에서 right 가 이동 하면서 need, missing 을 갱신하고
            // missing 이 0이 되면 다시 minLength 를 갱신할 수 있는지 확인하게 된다
            need.put(s.charAt(left), need.getOrDefault(s.charAt(left), 0) + 1);
            missing += 1;
            left += 1;

        }
        return s.substring(start, end);
    }
}
