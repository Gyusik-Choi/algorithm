import java.util.ArrayDeque;
import java.util.Deque;

public class ImplementQueueUsingStacks232 {
    Deque<Integer> stack1 = new ArrayDeque<>();
    Deque<Integer> stack2 = new ArrayDeque<>();

    public void push(int x) {
        stack1.push(x);
    }

    public int pop() {
        while (!stack1.isEmpty()) {
            stack2.push(stack1.pop());
        }
        int answer = stack2.pop();
        while (!stack2.isEmpty()) {
            stack1.push(stack2.pop());
        }
        return answer;
    }

    public int peek() {
        while (!stack1.isEmpty()) {
            stack2.push(stack1.pop());
        }
        int answer = stack2.element();
        while (!stack2.isEmpty()) {
            stack1.push(stack2.pop());
        }
        return answer;
    }

    public boolean empty() {
        return stack1.isEmpty();
    }
}
