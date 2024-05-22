import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        Main main = new Main();
        main.solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] gradeInfo = new int[N + 1][N + 1];
        int limitNumber = 501;

        for (int i = 1; i < N + 1; i++) {
            for (int j = 1; j < N + 1; j++) {
                if (i != j) {
                    gradeInfo[i][j] = limitNumber;
                }
            }
        }

        for (int i = 0; i < M; i++) {
            StringTokenizer students = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(students.nextToken());
            int B = Integer.parseInt(students.nextToken());
            gradeInfo[B][A] = 1;
        }

        floydWarshall(gradeInfo);
        System.out.println(countStudents(gradeInfo, limitNumber));
    }

    public void floydWarshall(int[][] grade) {
        for (int k = 1; k < grade.length; k++) {
            for (int i = 1; i < grade.length; i++) {
                for (int j = 1; j < grade.length; j++) {
                    grade[i][j] = Math.min(grade[i][j], grade[i][k] + grade[k][j]);
                }
            }
        }
    }

    public int countStudents(int[][] grade, int limit) {
        int cnt = 0;

        for (int i = 1; i < grade.length; i++) {
            boolean isCanCount = true;

            for (int j = 1; j < grade.length; j++) {
                // i 와 j 가 같은 경우는 0 이라
                // if 문을 충족하지 않는다
                if (grade[i][j] == limit && grade[j][i] == limit) {
                    isCanCount = false;
                    break;
                }
            }

            if (isCanCount) {
                cnt += 1;
            }
        }

        return cnt;
    }
}
