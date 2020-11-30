import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class B_4153 {
    
    public static void main(String[] args) throws IOException {

        while (true) {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            int sums1 = 0;
            int sums2 = 0;
            for (int i = 0; i < 3; i++) {
                if (i == 2) {
                    int num = Integer.parseInt(st.nextToken());
                    int squared = (int) Math.pow(num, 2);
                    sums2 += squared;
                } else {
                    int num = Integer.parseInt(st.nextToken());
                    int squared = (int) Math.pow(num, 2);
                    sums1 += squared;
                }

            }
            if (sums1 == 0) {
                break;
            } else if (sums1 == sums2) {
                System.out.println("right");
            } else {
                System.out.println("wrong");
            }
        }
        
    }
}