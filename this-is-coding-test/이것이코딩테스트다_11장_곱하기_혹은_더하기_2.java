import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String strNums = br.readLine();
        int[] nums = Arrays
                .stream(strNums.split(""))
                .mapToInt(Integer::parseInt)
                .toArray();

//        https://www.baeldung.com/java-stream-reduce
        int sums = Arrays
                .stream(nums)
                .reduce(0,
                        (acc, cur) -> acc < 2 || cur < 2 ? acc + cur : acc * cur);
        System.out.println(sums);
    }
}
