import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        Main main = new Main();
        main.solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer barnData = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(barnData.nextToken());
        int M = Integer.parseInt(barnData.nextToken());
        HashMap<Integer, ArrayList<Barn>> barns = new HashMap<Integer, ArrayList<Barn>>();

        for (int i = 0; i < M; i++) {
            StringTokenizer edge = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(edge.nextToken());
            int B = Integer.parseInt(edge.nextToken());

            ArrayList<Barn> list;
            if (barns.containsKey(A)) {
                list = barns.get(A);
            } else {
                list = new ArrayList<Barn>();
            }
            list.add(new Barn(1, B));
            barns.put(A, list);

            ArrayList<Barn> list2;
            if (barns.containsKey(B)) {
                list2 = barns.get(B);
            } else {
                list2 = new ArrayList<Barn>();
            }
            list2.add(new Barn(1, A));
            barns.put(B, list2);
        }

        dijkstra(N, 1, barns);
    }

    public void dijkstra(int n, int go, HashMap<Integer, ArrayList<Barn>> barnInfo) {
        boolean[] visited = new boolean[n + 1];
        int[] distances = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            distances[i] = Integer.MAX_VALUE;
        }

        distances[go] = 0;
        PriorityQueue<Barn> pq = new PriorityQueue<Barn>();
        pq.add(new Barn(distances[go], go));

        while (!pq.isEmpty()) {
            Barn start = pq.poll();

            if (visited[start.number]) {
                continue;
            }

            visited[start.number] = true;

            for (Barn end : barnInfo.get(start.number)) {
                if (visited[end.number]) {
                    continue;
                }

                if (distances[end.number] <= start.distance + end.distance) {
                    continue;
                }

                distances[end.number] = start.distance + end.distance;
                pq.add(new Barn(distances[end.number], end.number));
            }
        }

        System.out.println(Arrays.toString(findAnswer(distances)));
    }

    public int[] findAnswer(int[] distance) {
        // 최대 길이를 구하고
        // 최대 길이의 번호
        // 최대 길이의 갯수를 구한다
        int maxDistance = Arrays.stream(distance).max().getAsInt();
        // https://www.baeldung.com/java-array-find-index
        int maxNum = IntStream.range(0, distance.length).filter(d -> distance[d] == maxDistance).findFirst().getAsInt();
        int maxNumCnt = (int) Arrays.stream(distance).filter(d -> d == maxDistance).count();
        return new int[]{maxNum, maxDistance, maxNumCnt};
    }

    static class Barn implements Comparable<Barn> {
        int distance;
        int number;

        Barn(int distance, int number) {
            this.distance = distance;
            this.number = number;
        }

        @Override
        public int compareTo(Barn b) {
            return this.distance - b.distance;
        }
    }
}