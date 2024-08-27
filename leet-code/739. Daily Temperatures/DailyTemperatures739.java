import java.util.ArrayDeque;
import java.util.Deque;

public class DailyTemperatures739 {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] answer = new int[temperatures.length];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int cur = 0; cur < temperatures.length; cur++) {
            while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[cur]) {
                int prev = stack.pop();
                answer[prev] = cur - prev;
            }
            stack.push(cur);
        }
        return answer;
    }
}
