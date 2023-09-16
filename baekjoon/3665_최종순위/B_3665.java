import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Main main = new Main();
        main.solution();
    }

    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private void solution() throws IOException {
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            System.out.println(eachSolution());
        }
    }

    private String eachSolution() throws IOException {
        int n = Integer.parseInt(br.readLine());
        StringTokenizer rank = new StringTokenizer(br.readLine());

        int[] inDegree = new int[n + 1];
        ArrayList<Integer> tempRank = new ArrayList<>();
        int[][] priority = new int[n + 1][n + 1];

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(rank.nextToken());
            inDegree[num] = i;
            tempRank.add(num);
        }

        for (int i = 0; i < tempRank.size() - 1; i++) {
            int from = tempRank.get(i);

            for (int j = i + 1; j < tempRank.size(); j++) {
                int to = tempRank.get(j);
                priority[from][to] = 1;
            }
        }

        int m = Integer.parseInt(br.readLine());

        for (int i = 0; i < m; i++) {
            StringTokenizer changedRank = new StringTokenizer(br.readLine());
            int team1 = Integer.parseInt(changedRank.nextToken());
            int team2 = Integer.parseInt(changedRank.nextToken());

//             inDegree 로 아래처럼 비교할 경우
//             inDegree[team1] == inDegree[team2] 인 경우를
//             제대로 고려하지 못하고 else 문으로 들어간다
//             5
//             5 4 3 2 1
//             2
//             2 4
//             3 4
//             해당 입력에서
//             차수 정보는 [0, 1, 2, 3, 4] 인데
//             2 4 에서 [0, 2, 2, 2, 4] 가 되고
//             3 4 에서 3 과 4 의 차수가 같다
//
//             inDegree 는 차수 정보만 갖고 있고
//             둘 사이의 상대적인 우선 순위는 제대로 파악할 수 없다
//             (위에서 본 것처럼 차수 정보가 같으면 어떤게 우선 순위가 높은지 알 수 없다)
//             inDegree 는 같은 경우도 있기 때문에
//             차수 정보로 우선 순위를 파악하지 않고
//             서로 간의 우선 순위가 항상 구분이 되도록
//             별도로 우선 순위를 판단해야 한다
//
//            if (inDegree[team1] > inDegree[team2]) {
//                inDegree[team1] -= 1;
//                inDegree[team2] += 1;
//            } else {
//                inDegree[team1] += 1;
//                inDegree[team2] -= 1;
//            }

            if (priority[team1][team2] == 1) {
                priority[team1][team2] = 0;
                priority[team2][team1] = 1;

                inDegree[team1] += 1;
                inDegree[team2] -= 1;
            } else {
                priority[team1][team2] = 1;
                priority[team2][team1] = 0;

                inDegree[team1] -= 1;
                inDegree[team2] += 1;
            }
        }

        ArrayList<Integer> list = topologySort(inDegree, priority);

        if (list.isEmpty()) {
            return "IMPOSSIBLE";
        }

        StringBuilder sb = new StringBuilder();

        for (Integer integer : list) {
            sb.append(integer);
            sb.append(" ");
        }

        return sb.toString();
    }

    private ArrayList<Integer> topologySort(int[] degree, int[][] priorityInfo) {
        int go = findStart(degree);

        if (go == -1) {
            return new ArrayList<>();
        }

        Deque<Integer> deq = new ArrayDeque<>();
        deq.add(go);
        ArrayList<Integer> answer = new ArrayList<>();

        while (!deq.isEmpty()) {
            int start = deq.pollFirst();

            answer.add(start);

            for (int end = 1; end < degree.length; end++) {
                if (priorityInfo[start][end] == 1) {
                    degree[end] -= 1;

                    if (degree[end] == 0) {
                        deq.add(end);
                    }
                }
            }
        }

        if (isCycle(degree)) {
            return new ArrayList<>();
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
        for (int i = 1; i < degree.length; i++) {
            if (degree[i] != 0) {
                return true;
            }
        }

        return false;
    }
}
