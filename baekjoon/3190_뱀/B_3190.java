import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int K = Integer.parseInt(br.readLine());
        // 빈칸 0, 사과 1, 뱀 2
        int[][] board = new int[N][N];

        for (int i = 0; i < K; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int y = Integer.parseInt(st.nextToken()) - 1;
            int x = Integer.parseInt(st.nextToken()) - 1;
            board[y][x] = 1;
        }

        int L = Integer.parseInt(br.readLine());
        Deque<int[]> moveHistory = new ArrayDeque<int[]>();
        Deque<Direction> deq = new ArrayDeque<Direction>();

        for (int i = 0; i < L; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int X = Integer.parseInt(st.nextToken());
            String C = st.nextToken();
            deq.add(new Direction(X, C));
        }

        int seconds = 0;
        // 상, 우, 하, 좌
        int[] yValue = {-1, 0, 1, 0};
        int[] xValue = {0, 1, 0, -1};

        // 초기 방향은 우
        int curDirection = 1;
        int curY = 0;
        int curX = 0;

        // 뱀을 시작 위치에 놓는다
        board[curY][curX] = 2;
        moveHistory.add(new int[]{0, 0});
        int[] arr = moveHistory.peekFirst();

        while (true) {
            seconds += 1;

            curY = yValue[curDirection] + curY;
            curX = xValue[curDirection] + curX;

            // 벽에 부딪힘
            if (0 > curY || curY >= N || 0 > curX || curX >= N) {
                break;
            }

            // 자기자신과 부딪힘
            if (board[curY][curX] == 2) {
                break;
            }

            // 사과가 없다면
            if (board[curY][curX] == 0) {
                int[] history = moveHistory.pollFirst();
                assert history != null;
                board[history[0]][history[1]] = 0;
            }

            moveHistory.add(new int[]{curY, curX});

            // 방향 바꿔야 한다면
            if (deq.size() > 0 && deq.peekFirst().sec == seconds) {
                Direction direction = deq.pollFirst();

                if (direction.dir.equals("L")) {
                    curDirection = (curDirection + 3) % 4;
                } else {
                    curDirection = (curDirection + 1) % 4;
                }
            }

            board[curY][curX] = 2;
        }

        System.out.println(seconds);
    }

    public static class Direction {
        int sec;
        String dir;

        Direction(int sec, String dir) {
            this.sec = sec;
            this.dir = dir;
        }
    }
}

// 참고
// https://velog.io/@esun1903/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-Deque
