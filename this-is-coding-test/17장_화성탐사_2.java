import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Main main = new Main();
        main.solution();
    }

    public BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public void solution() throws IOException {
        int T = Integer.parseInt(br.readLine());

        for (int k = 0; k < T; k++) {
            runCase();
        }
    }

    public void runCase() throws IOException {
        int N = Integer.parseInt(br.readLine());
        int[][] distanceArr = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            for (int j = 0; j < N; j++) {
                int distance = Integer.parseInt(st.nextToken());
                distanceArr[i][j] = distance;
            }
        }

        HashMap<Integer, ArrayList<Node>> nodes = getNodes(distanceArr);
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(distanceArr[0][0], 0));
        boolean[] visited = new boolean[N * N];
        int[] distances = new int[N * N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                distances[i * N + j] = Integer.MAX_VALUE;
            }
        }
        distances[0] = distanceArr[0][0];

        while (!pq.isEmpty()) {
            Node start = pq.poll();

            if (visited[start.number]) {
                continue;
            }

            visited[start.number] = true;

            for (Node end : nodes.get(start.number)) {
                if (visited[end.number]) {
                    continue;
                }

                if (distances[end.number] <= start.distance + end.distance) {
                    continue;
                }

                distances[end.number] = start.distance + end.distance;
                pq.add(new Node(distances[end.number], end.number));
            }
        }

        System.out.println(distances[N * N - 1]);
    }

    private HashMap<Integer, ArrayList<Node>> getNodes(int[][] arr) {
        HashMap<Integer, ArrayList<Node>> nodes = new HashMap<>();
        int[] yValue = new int[]{-1, 0, 1, 0};
        int[] xValue = new int[]{0, 1, 0, -1};

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                // 세로축 인덱스 * arr 길이 + 가로축 인덱스
                // ex>
                // 3 X 3 배열의 경우
                // 0 1 2
                // 3 4 5
                // 6 7 8
                int startNum = i * arr.length + j;

                for (int k = 0; k < 4; k++) {
                    int y = i + yValue[k];
                    int x = j + xValue[k];

                    if (0 > y || y >= arr.length || 0 > x || x >= arr.length) {
                        continue;
                    }

                    int endNum = y * arr.length + x;

                    ArrayList<Node> list;
                    if (nodes.containsKey(startNum)) {
                        list = nodes.get(startNum);
                    } else {
                        list = new ArrayList<>();
                    }
                    list.add(new Node(arr[y][x], endNum));
                    nodes.put(startNum, list);
                }
            }
        }

        return nodes;
    }

    static class Node implements Comparable<Node> {
        int distance;
        int number;

        Node(int distance, int number) {
            this.distance = distance;
            this.number = number;
        }

        @Override
        public int compareTo(Node o) {
            return this.distance - o.distance;
        }
    }
}
