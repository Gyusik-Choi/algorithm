import java.util.ArrayDeque;
import java.util.Deque;

public class TrappingRainWater42_2 {
    public int trap(int[] height) {
        Deque<Integer> stack = new ArrayDeque<>();
        int sums = 0;

        for (int i = 0; i < height.length; i++) {
            while (!stack.isEmpty() && height[i] > height[stack.peek()]) {
                Integer top = stack.pop();

                if (stack.isEmpty()) break;

                int distance = i - stack.peek() - 1;
                int waters = Math.min(height[i], height[stack.peek()]) - height[top];
                sums += distance * waters;
            }

            stack.push(i);
        }

        return sums;
    }
}
