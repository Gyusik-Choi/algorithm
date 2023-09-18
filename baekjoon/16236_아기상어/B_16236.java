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
        int N = Integer.parseInt(br.readLine());
        int[][] sea = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            for (int j = 0; j < N; j++) {
                int num = Integer.parseInt(st.nextToken());
                sea[i][j] = num;
            }
        }

        System.out.println(littleShark(sea));
    }

    private int littleShark(int[][] seaInfo) {
        int totalTime = 0;
        int sharkSize = 2;
        int fishCnt = 0;

        while (true) {
            // 상어 찾기
            int[] shark = findShark(seaInfo);

            // 물고기 찾기
            ArrayList<Fish> fishes = findFish(seaInfo, shark, sharkSize);

            // 물고기 없으면 종료
            if (fishes.isEmpty()) {
                break;
            }

            Fish fish = fishes.get(0);

            // 상어 이동
            sharkMove(seaInfo, shark, fish);

            // 이동 시간 더하기
            totalTime += fish.distance;

            // 물고기 수 더하기
            fishCnt += 1;

            // 물고기 수와 상어의 크기 같은 경우
            if (fishCnt == sharkSize) {
                fishCnt = 0;
                sharkSize += 1;
            }
        }

        return totalTime;
    }

    private int[] findShark(int[][] seaInfo) {
        for (int i = 0; i < seaInfo.length; i++) {
            for (int j = 0; j < seaInfo.length; j++) {
                if (seaInfo[i][j] == 9) {
                    return new int[]{i, j};
                }
            }
        }

        return new int[]{-1, -1};
    }

    private ArrayList<Fish> findFish(int[][] seaInfo, int[] shark, int sharkSize) {
        int n = seaInfo.length;
        int[] yValue = new int[]{-1, 0, 1, 0};
        int[] xValue = new int[]{0, 1, 0, -1};

        boolean[][] visited = new boolean[n][n];
        visited[shark[0]][shark[1]] = true;
        ArrayList<Fish> fishList = new ArrayList<>();
        Deque<Fish> deq = new ArrayDeque<>();
        // 거리, y, x
        deq.add(new Fish(0, shark[0], shark[1]));

        while (!deq.isEmpty()) {
            Fish start = deq.pollFirst();

            int dist = start.distance;
            int sharkY = start.y;
            int sharkX = start.x;

            for (int i = 0; i < 4; i++) {
                int y = sharkY + yValue[i];
                int x = sharkX + xValue[i];

                // 공간 벗어난 경우
                if (y < 0 || y >= n || x < 0 || x >= n) {
                    continue;
                }

                // 이미 방문한 경우
                if (visited[y][x]) {
                    continue;
                }

                // 상어 크기 보다 큰 경우
                if (seaInfo[y][x] > sharkSize) {
                    continue;
                }

                // 상어 크기 보다 작거나 같은 경우만 이동 가능
                if (seaInfo[y][x] <= sharkSize) {
                    visited[y][x] = true;
                    deq.add(new Fish(dist + 1, y, x));

                    if (seaInfo[y][x] > 0 && seaInfo[y][x] < sharkSize) {
                        fishList.add(new Fish(dist + 1, y, x));
                    }
                }
            }
        }

        Collections.sort(fishList);
        return fishList;
    }

    private void sharkMove(int[][] seaInfo, int[] cur, Fish next) {
        seaInfo[cur[0]][cur[1]] = 0;
        seaInfo[next.y][next.x] = 9;
    }
}

class Fish implements Comparable<Fish> {
    int distance;
    int y;
    int x;

    Fish(int distance, int y, int x) {
        this.distance = distance;
        this.y = y;
        this.x = x;
    }

    @Override
    public int compareTo(Fish f) {
        if (this.distance == f.distance) {
            if (this.y == f.y) {
                return this.x - f.x;
            }

            return this.y - f.y;
        }

        return this.distance - f.distance;
    }
}
