import java.util.Comparator;
import java.util.PriorityQueue;

public class KClosestPointsToOrigin973 {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Point> pq = new PriorityQueue<>(Comparator.comparingInt(p -> p.distance));
        for (int[] point : points) {
            pq.add(new Point(point));
        }

        int[][] answer = new int[k][2];
        for (int i = 0; i < k; i++) {
            answer[i] = pq.poll().idx;
        }
        return answer;
    }

    private static class Point {
        int[] idx;
        int distance;

        Point(int[] idx) {
            this.idx = idx;
            distance = (idx[0] * idx[0]) + (idx[1] * idx[1]);
        }
    }
}
