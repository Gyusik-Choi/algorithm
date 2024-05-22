import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        ArrayList<Integer> adventurers = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            int adventurer = Integer.parseInt(st.nextToken());
            adventurers.add(adventurer);
        }

        Collections.sort(adventurers);

        int group = 0;
        int cnt = 0;

        for (int i = 0; i < N; i++) {
            cnt += 1;

            if (adventurers.get(i) == cnt) {
                group += 1;
                cnt = 0;
            };
        }

        System.out.println(group);
    }
}