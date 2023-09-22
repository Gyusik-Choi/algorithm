import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        Solution solution = new Solution();
        solution.solution();
    }
}

class Solution {

    private int maxValue = 0;

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] fishInfo = new int[4][4];
        int[][] directionInfo = new int[4][4];

        for (int i = 0; i < 4; i++) {
            StringTokenizer row = new StringTokenizer(br.readLine());

            for (int j = 0; j < 4; j++) {
                int fishNum = Integer.parseInt(row.nextToken());
                int directionNum = Integer.parseInt(row.nextToken());

                fishInfo[i][j] = fishNum;
                directionInfo[i][j] = directionNum;
            }
        }

        move(fishInfo, directionInfo, new Shark(0, 0), new Fish(0, 0), 0);
        System.out.println(maxValue);
    }

    // 재귀
    // 파라미터 => 물고기 정보, 방향 정보, 상어 위치, 상어 이동할 위치, 물고기 번호 누적 합
    // 빈 칸 -1, 상어 0, 물고기 1 ~ 16
    private void move(int[][] fishes, int[][] direction, Shark shark, Fish fish, int sums) {
        // 상어 이동
        sums += moveShark(fishes, shark, fish);

        maxValue = Math.max(maxValue, sums);

        // 물고기 이동
        moveFish(fishes, direction);

        // 상어 이동 가능한 위치를
        // for 문 돌면서 하나씩 재귀 호출
        // 기존 상어 위치가 아니라
        // 이동한 상어 위치를 기준으로 찾아야 한다
        ArrayList<Fish> fishList = findSharkCanMove(fishes, direction, new Shark(fish.y, fish.x));

        for (Fish candidate : fishList) {
            move(copyFish(fishes), copyDirection(direction), new Shark(fish.y, fish.x), candidate, sums);
        }
    }

    private int moveShark(int[][] fishes, Shark shark, Fish fish) {
        int fishNum = fishes[fish.y][fish.x];
        fishes[shark.y][shark.x] = -1;
        fishes[fish.y][fish.x] = 0;
        return fishNum;
    }

    private void moveFish(int[][] fishes, int[][] direction) {
        // 1번 부터 16번 까지
        for (int num = 1; num <= 16; num++) {
            Fish cur = findCurFish(fishes, num);

            if (cur.y == -1 && cur.x == -1) {
                continue;
            }

            Fish next = findNextFish(fishes, direction, cur);

            if (next.y == -1 && next.x == -1) {
                continue;
            }

            switchFish(fishes, direction, cur, next);
        }
    }

    private Fish findCurFish(int[][] fishes, int target) {
        for (int i = 0; i < fishes.length; i++) {
            for (int j = 0; j < fishes.length; j++) {
                if (fishes[i][j] == target) {
                    return new Fish(i, j);
                }
            }
        }

        return new Fish(-1, -1);
    }

    private Fish findNextFish(int[][] fishes, int[][] direction, Fish cur) {
        int[] yValue = new int[]{-1, -1, 0, 1, 1, 1, 0, -1};
        int[] xValue = new int[]{0, -1, -1, -1, 0, 1, 1, 1};

        int curY = cur.y;
        int curX = cur.x;
        int curDir = direction[curY][curX];

        for (int i = 0; i < 8; i++) {
            int curIdx = (curDir - 1) % 8;
            curDir += 1;

            int y = curY + yValue[curIdx];
            int x = curX + xValue[curIdx];

            if (0 > y || y >= fishes.length || 0 > x || x >= fishes.length) {
                continue;
            }

            if (fishes[y][x] == 0) {
                continue;
            }

            // 이동할 위치를 찾으면서 방향 값을 바꾸기 때문에
            // 새로운 방향 값으로 변경한다
            setNewDirectionValue(direction, cur, curIdx + 1);

            return new Fish(y, x);
        }

        return new Fish(-1, -1);
    }

    private void setNewDirectionValue(int[][] direction, Fish fish, int newDir) {
        direction[fish.y][fish.x] = newDir;
    }

    // 물고기, 방향 교환
    private void switchFish(int[][] fishes, int[][] direction, Fish cur, Fish next) {
        int curNum = fishes[cur.y][cur.x];
        fishes[cur.y][cur.x] = fishes[next.y][next.x];
        fishes[next.y][next.x] = curNum;

        int curDir = direction[cur.y][cur.x];
        direction[cur.y][cur.x] = direction[next.y][next.x];
        direction[next.y][next.x] = curDir;
    }

    private ArrayList<Fish> findSharkCanMove(int[][] fishes, int[][] direction, Shark shark) {
        int y = shark.y;
        int x = shark.x;

        int[] yValue = new int[]{-1, -1, 0, 1, 1, 1, 0, -1};
        int[] xValue = new int[]{0, -1, -1, -1, 0, 1, 1, 1};

        int dir = direction[y][x];

        ArrayList<Fish> moveList = new ArrayList<>();

        for (int i = 0; i < 3; i++) {
            y += yValue[dir - 1];
            x += xValue[dir - 1];

            if (0 > y || y >= fishes.length || 0 > x || x >= fishes.length) {
                continue;
            }

            if (fishes[y][x] > 0) {
                moveList.add(new Fish(y, x));
            }
        }

        return moveList;
    }

    private int[][] copyFish(int[][] fishes) {
        int[][] newFishes = new int[fishes.length][fishes.length];

        for (int i = 0; i < fishes.length; i++) {
            for (int j = 0; j < fishes.length; j++) {
                newFishes[i][j] = fishes[i][j];
            }
        }

        return newFishes;
    }

    private int[][] copyDirection(int[][] direction) {
        int[][] newDirection = new int[direction.length][direction.length];

        for (int i = 0; i < direction.length; i++) {
            for (int j = 0; j < direction.length; j++) {
                newDirection[i][j] = direction[i][j];
            }
        }

        return newDirection;
    }
}

class Shark {
    int y;
    int x;

    Shark(int y, int x) {
        this.y = y;
        this.x = x;
    }
}

class Fish {
    int y;
    int x;

    Fish(int y, int x) {
        this.y = y;
        this.x = x;
    }
}
