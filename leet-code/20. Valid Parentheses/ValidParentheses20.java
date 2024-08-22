import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

public class ValidParentheses20 {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap<>() {{
            put('(', ')');
            put('{', '}');
            put('[', ']');
        }};
        Deque<Character> deq = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            // 덱이 비었으면
            if (deq.isEmpty()) {
                // 닫는 괄호가 나오면 안 된다
                if (map.containsValue(c)) {
                    return false;
                }
                deq.add(c);
            // 덱이 비어있지 않으면
            } else {
                // 덱이 마지막 문자로 조회한 맵의 값이 c 와 동일하면
                // 덱에서 마지막 문자를 꺼낸다
                if (map.get(deq.peekLast()) == c) {
                    deq.pollLast();
                } else {
                    // 닫는 괄호가 나오면 안 된다
                    if (map.containsValue(c)) {
                        return false;
                    }
                    deq.add(c);
                }
            }
        }

        return deq.isEmpty();
    }
}
