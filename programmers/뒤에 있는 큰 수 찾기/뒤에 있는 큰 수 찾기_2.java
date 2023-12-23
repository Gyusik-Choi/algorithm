import java.util.Arrays;
import java.util.Stack;

public class Main {
    public static void main(String[] args){
        Solution solution = new Solution();
        int[] maps = {2, 3, 3, 5};
        System.out.println(Arrays.toString(solution.solution(maps)));
    }
}

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = Arrays
                .stream(new int[numbers.length])
                .map(v -> v - 1)
                .toArray();

        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < numbers.length; i++) {
            while (!stack.isEmpty() && numbers[stack.peek()] < numbers[i]) {
                answer[stack.pop()] = numbers[i];
            }
            stack.add(i);
        }

        while (!stack.isEmpty()) {
            answer[stack.pop()] = -1;
        }

        return answer;
    }
}
