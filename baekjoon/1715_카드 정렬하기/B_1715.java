import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<Integer>();

        for (int i = 0; i < N; i++) {
            priorityQueue.add(Integer.parseInt(br.readLine()));
        }

        int sums = 0;

        while (priorityQueue.size() >= 2) {
            int card1 = priorityQueue.poll();
            int card2 = priorityQueue.poll();
            sums += card1 + card2;
            priorityQueue.add(card1 + card2);
        }

        System.out.println(sums);
    }
}
