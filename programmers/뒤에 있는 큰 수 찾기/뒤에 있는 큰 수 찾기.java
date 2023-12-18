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
                .map(a -> a - 1)
                .toArray();

        Stack<Integer> stack = new Stack<>();

        for (int i = numbers.length - 1; i > -1; i--) {
            while (!stack.isEmpty()) {
                if (stack.peek() > numbers[i]) {
                    answer[i] = stack.peek();
                    break;
                } else {
                    stack.pop();
                }
            }

            if (stack.isEmpty()) {
                answer[i] = -1;
            }
            stack.add(numbers[i]);
        }

        return answer;
    }
}
