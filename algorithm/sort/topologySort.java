import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        Main main = new Main();
        main.solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer metaInfo = new StringTokenizer(br.readLine());
        int v = Integer.parseInt(metaInfo.nextToken());
        int e = Integer.parseInt(metaInfo.nextToken());

        // 간선 정보
        HashMap<Integer, ArrayList<Integer>> edgeInfo = new HashMap<>();

        // topologySort 함수 안의
        // edges.get(start) 부분에서 NullPointerException 에러가 발생하지 않도록
        // edgeInfo 에 1부터 v까지 정점을 키로 하는 빈 리스트를 값으로 넣는다
         for (int i = 1; i < v + 1; i++) {
             edgeInfo.put(i, new ArrayList<Integer>());
         }

        // 차수 정보
        int[] levels = new int[v + 1];

        for (int i = 0; i < e; i++) {
            StringTokenizer edge = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(edge.nextToken());
            int end = Integer.parseInt(edge.nextToken());

            ArrayList<Integer> lst = edgeInfo.get(start);
            lst.add(end);
            edgeInfo.put(start, lst);

            levels[end] += 1;
        }

        System.out.println(topologySort(edgeInfo, levels));
    }

    private ArrayList<Integer> topologySort(HashMap<Integer, ArrayList<Integer>> edges, int[] degree) {
        ArrayList<Integer> answer = new ArrayList<>();
        ArrayDeque<Integer> deq = new ArrayDeque<>();

        int go = findStart(degree);

        // 진입 차수가 0인 노드가
        // 처음부터 없어서 탐색을 시작할 수 없는 경우
        // (사이클 발생)
        if (go == -1) {
            return new ArrayList<Integer>();
        }

        answer.add(go);
        deq.add(go);

        while (!deq.isEmpty()) {
            int start = deq.pollFirst();

            for (int end : edges.get(start)) {
                degree[end] -= 1;

                if (degree[end] == 0) {
                    answer.add(end);
                    deq.add(end);
                }
            }
        }

        if (isCycle(degree)) {
            return new ArrayList<Integer>();
        }

        return answer;
    }

    private int findStart(int[] degree) {
        for (int i = 1; i < degree.length; i++) {
            if (degree[i] == 0) {
                return i;
            }
        }

        return -1;
    }

    private boolean isCycle(int[] degree) {
        return findStart(degree) == -1;
    }
}
