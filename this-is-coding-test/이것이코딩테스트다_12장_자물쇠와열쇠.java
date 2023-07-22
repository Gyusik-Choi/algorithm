class Solution {
    public static void main(String[] args) {
        Solution solution = new Solution();

        int[][] key = {{0, 0, 0}, {1, 0, 0}, {0, 1, 1}};
        int[][] lock = {{1, 1, 1}, {1, 1, 0}, {1, 0, 1}};
        boolean answer = solution.solution(key, lock);
        System.out.println(answer);
    }

    public boolean solution(int[][] key, int[][] lock) {
        int m = key.length;
        int n = lock.length;
        int arrLength = (m - 1) * 2 + n;

        for (int k = 0; k < 4; k++) {
            // 열쇠 회전
            // 회전한 열쇠에서 다시 회전해야 90도씩 회전할 수 있어서
            // 회전한 값을 key 에 대입해서 key 를 변경
            key = rotateKey(key, m);

            for (int i = 0; i < arrLength - (m - 1); i++) {
                for (int j = 0; j < arrLength - (m - 1); j++) {
                    // 열쇠와 자물쇠를 합친 배열 새로 생성한다
                    int[][] arr = initArr(arrLength);
                    // 배열에 자물쇠를 놓는다
                    setLock(arr, lock, m, n);
                    // 배열에 열쇠를 놓는다
                    // 열쇠를 놓을때 기존 배열의 값과 더한다
                    addKey(arr, key, i, j);

                    // 자물쇠를 열 수 있으면 탐색 종료
                    if (isUnlock(arr, m, n)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }

    public int[][] rotateKey(int[][] key, int m) {
        int[][] rotatedKey = new int[m][m];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                rotatedKey[i][j] = key[j][m - i - 1];
            }
        }

        return rotatedKey;
    }

    public int[][] initArr(int arrLength) {
         return new int[arrLength][arrLength];
    }

    public void setLock(int[][] arr, int[][] lock, int m, int n) {
        for (int i = m - 1; i < m - 1 + n; i++) {
            for (int j = m - 1; j < m - 1 + n; j++) {
                arr[i][j] = lock[i - (m - 1)][j - (m - 1)];
            }
        }
    }

    public void addKey(int[][] arr, int[][] key, int y, int x) {
        for (int i = y; i < y + key.length; i++) {
            for (int j = x; j < x + key.length; j++) {
                arr[i][j] += key[i - y][j - x];
            }
        }
    }

    public boolean isUnlock(int[][] arr, int m, int n) {
        for (int i = m - 1; i < m - 1 + n; i++) {
            for (int j = m - 1; j < m - 1 + n; j++) {
                if (arr[i][j] != 1) {
                    return false;
                }
            }
        }

        return true;
    }
}
