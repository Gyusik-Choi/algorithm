import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());

        // N 크기 만큼 2차원 열을 만들면 최대 크기가 900억이라 메모리 초과가 발생한다
        // 공간을 줄이기 위해 2차원 ArrayList 를 만들고 해당하는 도시 정보만 추가한다
        ArrayList<ArrayList<Integer>> cityList = new ArrayList<ArrayList<Integer>>();

        for (int i = 0; i <= N; i++) {
            cityList.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < M; i++) {
            StringTokenizer edge = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(edge.nextToken());
            int B = Integer.parseInt(edge.nextToken());
            cityList.get(A).add(B);
        }

        ArrayDeque<int[]> deq = new ArrayDeque<>();
        deq.add(new int[]{X, 0});

        boolean[] visited = new boolean[N + 1];
        visited[X] = true;

        System.out.println(bfs(deq, cityList, visited, N, K));
        br.close();
    }

    private static StringBuilder bfs(ArrayDeque<int[]> deq, ArrayList<ArrayList<Integer>> cities, boolean[] visited, int n, int targetDistance) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        StringBuilder sb = new StringBuilder();

        while (!deq.isEmpty()) {
            int[] cityInfo = deq.pollFirst();
            int start = cityInfo[0];
            int distance = cityInfo[1];

            if (distance > targetDistance) {
                break;
            }

            if (distance == targetDistance) {
                answer.add(start);
            }

            for (int end: cities.get(start)) {
                if (visited[end]) {
                    continue;
                }

                deq.add(new int[]{end, distance + 1});
                visited[end] = true;
            }
        }

        if (!answer.isEmpty()) {
            Collections.sort(answer);

            for (int a: answer) {
                sb.append(a).append("\n");
            }
        } else {
            sb.append(-1).append("\n");
        }

        sb.deleteCharAt(sb.length() - 1);
        return sb;
    }
}
