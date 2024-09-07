import java.util.PriorityQueue;

public class Programmers42626 {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i : scoville) pq.add(i);

        int cnt = 0;
        while (pq.size() > 1 && pq.peek() < K) {
            pq.add(pq.poll() + (pq.poll() * 2));
            cnt += 1;
        }

        if (pq.peek() >= K) return cnt;
        return -1;
    }
}
