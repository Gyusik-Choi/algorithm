import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Main main = new Main();
        int answer = main.solution();
        System.out.println(answer);
    }

    public int solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer villageMetaData = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(villageMetaData.nextToken());
        int M = Integer.parseInt(villageMetaData.nextToken());
        int totalRoadDistance = 0;

        HashMap<Integer, ArrayList<House>> roadInfo = new HashMap<>();
        for (int i = 0; i < M; i++) {
            StringTokenizer road = new StringTokenizer(br.readLine());

            int X = Integer.parseInt(road.nextToken());
            int Y = Integer.parseInt(road.nextToken());
            int Z = Integer.parseInt(road.nextToken());
            totalRoadDistance += Z;

            ArrayList<House> list;
            if (roadInfo.containsKey(X)) {
                list = roadInfo.get(X);
            } else {
                list = new ArrayList<>();
            }
            list.add(new House(Z, Y));
            roadInfo.put(X, list);

            ArrayList<House> list2;
            if (roadInfo.containsKey(Y)) {
                list2 = roadInfo.get(Y);
            } else {
                list2 = new ArrayList<>();
            }
            list2.add(new House(Z, X));
            roadInfo.put(Y, list2);
        }

        return totalRoadDistance - mst(N, roadInfo);
    }

    // prim 알고리즘 활용
    private int mst(int n, HashMap<Integer, ArrayList<House>> roads) {
        boolean[] selected = new boolean[n];
        PriorityQueue<House> pq = new PriorityQueue<>();
        int[] distance = new int[n];
        Arrays.fill(distance, Integer.MAX_VALUE);

        pq.add(new House(0, 0));
        distance[0] = 0;
        int minRoadDistance = 0;

        while (!pq.isEmpty()) {
            House start = pq.poll();

            if (selected[start.number]) {
                continue;
            }

            selected[start.number] = true;
            minRoadDistance += start.distance;

            for (House end : roads.get(start.number)) {
                if (distance[end.number] > end.distance) {
                    distance[end.number] = end.distance;
                    pq.add(new House(end.distance, end.number));
                }
            }
        }

        return minRoadDistance;
    }

    static class House implements Comparable<House> {
        int distance;
        int number;

        House(int distance, int number) {
            this.distance = distance;
            this.number = number;
        }

        @Override
        public int compareTo(House h) {
            return this.distance - h.distance;
        }
    }
}
