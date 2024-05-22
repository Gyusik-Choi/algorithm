import java.util.ArrayList;

class Solution {
    int length;

    boolean[][] pillar;
    boolean[][] beam;

    public int[][] solution(int n, int[][] buildFrame) {
        length = n;
        pillar = new boolean[n + 1][n + 1];
        beam = new boolean[n + 1][n + 1];
        int cnt = 0;

        for (int[] frame: buildFrame) {
            // 삭제
            if (frame[3] == 0) {
                removeFrame(frame);
                cnt -= 1;

                if (isPossible()) {
                    continue;
                }

                addFrame(frame);
                cnt += 1;
                // 설치
            } else {
                addFrame(frame);
                cnt += 1;

                if (isPossible()) {
                    continue;
                }

                removeFrame(frame);
                cnt -= 1;
            }
        }

        int[][] answer = new int[cnt][3];
        int idx = 0;

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                if (pillar[i][j]) {
                    answer[idx][0] = i;
                    answer[idx][1] = j;
                    answer[idx][2] = 0;
                    idx += 1;
                }

                if (beam[i][j]) {
                    answer[idx][0] = i;
                    answer[idx][1] = j;
                    answer[idx][2] = 1;
                    idx += 1;
                }
            }
        }

        return answer;
    }

    private void removeFrame(int[] frame) {
        if (frame[2] == 0) {
            pillar[frame[0]][frame[1]] = false;
        } else {
            beam[frame[0]][frame[1]] = false;
        }
    }

    private void addFrame(int[] frame) {
        if (frame[2] == 0) {
            pillar[frame[0]][frame[1]] = true;
        } else {
            beam[frame[0]][frame[1]] = true;
        }
    }

    private boolean isPossible() {
        for (int i = 0; i <= length; i++) {
            for (int j = 0; j <= length; j++) {
                if (pillar[i][j] && !isPillarPossible(new int[]{i, j, 0})) {
                    return false;
                }

                if (beam[i][j] && !isBeamPossible(new int[]{i, j, 1})) {
                    return false;
                }
            }
        }

        return true;
    }

    private boolean isPillarPossible(int[] frame) {
        // 바닥
        if (frame[1] == 0) {
            return true;
        }

        // 아래에 기둥
        if (frame[1] > 0 && pillar[frame[0]][frame[1] - 1]) {
            return true;
        }

        // 왼쪽에 보
        if (frame[0] > 0 && beam[frame[0] - 1][frame[1]]) {
            return true;
        }

        // 오른쪽에 보
        if (beam[frame[0]][frame[1]]) {
            return true;
        }

        return false;
    }

    private boolean isBeamPossible(int[] frame) {
        // 왼쪽 아래에 기둥
        if (frame[1] > 0 && pillar[frame[0]][frame[1] - 1]) {
            return true;
        }

        // 오른쪽 아래에 기둥
        if (frame[0] < length && frame[1] > 0 && pillar[frame[0] + 1][frame[1] - 1]) {
            return true;
        }

        // 왼쪽과 오른쪽에 보
        if (
            frame[0] > 0 &&
            beam[frame[0] - 1][frame[1]] &&
            frame[0] < length &&
            beam[frame[0] + 1][frame[1]]
        ) {
            return true;
        }

        return false;
    }
}
