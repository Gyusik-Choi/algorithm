import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

public class ValidParentheses20_2 {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap<>() {{
            put('(', ')');
            put('{', '}');
            put('[', ']');
        }};
        // ArrayDeque 의 스택 연산을 활용 (push, pop)
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            // 닫는 괄호가 아닌 경우
            if (!map.containsValue(c)) {
                stack.push(c);
            } else {
                // 스택이 비었거나 혹은 스택에서 꺼낸 값으로 조회한 맵의 값이 c 와 다른 경우
                if (stack.isEmpty() || map.get(stack.pop()) != c) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
