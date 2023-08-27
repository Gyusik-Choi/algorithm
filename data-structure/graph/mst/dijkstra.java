import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Main main = new Main();
        main.dijkstra();
    }

    // 정점 0을 기준으로 최소 거리
    public void dijkstra() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer nodeInfo = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(nodeInfo.nextToken());
        int E = Integer.parseInt(nodeInfo.nextToken());
        HashMap<Integer, ArrayList<Node>> nodes = new HashMap<>();

        for (int i = 0; i < E; i++) {
            StringTokenizer edgeInfo = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(edgeInfo.nextToken());
            int b = Integer.parseInt(edgeInfo.nextToken());
            int c = Integer.parseInt(edgeInfo.nextToken());

            // a
            ArrayList<Node> arr;
            if (nodes.containsKey(a)) {
                arr = nodes.get(a);
            } else {
                arr = new ArrayList<>();
            }
            arr.add(new Node(c, b));
            nodes.put(a, arr);

            // b
            ArrayList<Node> arr2;
            if (nodes.containsKey(b)) {
                arr2 = nodes.get(b);
            } else {
                arr2 = new ArrayList<>();
            }
            arr2.add(new Node(c, a));
            nodes.put(b, arr2);
        }

        boolean[] visited = new boolean[V];
        int[] distances = new int[V];
        // distances 최대값으로 초기화
        Arrays.fill(distances, Integer.MAX_VALUE);
        // 출발점 0은 거리 값을 0으로 초기화
        distances[0] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        // 거리, 정점
        // 정점 0이 출발점
        pq.add(new Node(distances[0], 0));

        while (!pq.isEmpty()) {
            Node startNode = pq.poll();
            int startDist = startNode.distance;
            int start = startNode.number;

            if (visited[start]) {
                continue;
            }

            visited[start] = true;

            for (Node endNode : nodes.get(start)) {
                int endDist = endNode.distance;
                int end = endNode.number;

                if (!visited[end] && distances[end] > startDist + endDist) {
                    distances[end] = startDist + endDist;
                    System.out.println(Arrays.toString(new int[]{distances[end], end}));
                    pq.add(new Node(distances[end], end));
                }
            }
        }

        System.out.println(Arrays.toString(distances));
    }

    static class Node implements Comparable<Node> {
        int distance;
        int number;

        Node(int distance, int number) {
            this.distance = distance;
            this.number = number;
        }

        // PriorityQueue 가 원하는 순서로 정렬될 수 있도록
        // 정렬할 기준을 작성한다
        // (Python 과 달리 PriorityQueue 에 배열을 넣으면 알아서 정렬되지 못한다)
        @Override
        public int compareTo(Node n) {
            if (this.distance == n.distance) {
                return this.number - n.number;
            }

            return this.distance - n.distance;
        }
    }
}
