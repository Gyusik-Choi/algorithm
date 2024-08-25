import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

public class RemoveDuplicateLetters316 {
    public String removeDuplicateLetters(String s) {
        Map<Character, Integer> counter = new HashMap<>();
        Map<Character, Boolean> complete = new HashMap<>();
        Deque<Character> stack = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            if (counter.containsKey(c)) {
                counter.put(c, counter.get(c) + 1);
            } else {
                counter.put(c, 1);
            }
        }

        for (char c : s.toCharArray()) {
            counter.put(c, counter.get(c) - 1);

            if (complete.containsKey(c) && complete.get(c)) {
                continue;
            }

            while (!stack.isEmpty() && stack.peek() > c && counter.get(stack.peek()) > 0) {
                complete.put(stack.pop(), false);
            }

            complete.put(c, true);
            stack.push(c);
        }

        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pollLast());
        }
        return sb.toString();
    }
}
