import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Combinations77 {
    public List<List<Integer>> combine(int n, int k) {
        return dfsRecursive(new ArrayList<>(), new int[k], n, 1, 0);
    }

    private List<List<Integer>> dfsRecursive(List<List<Integer>> combs, int[] comb, int limit, int start, int arrayIdx) {
        if (arrayIdx >= comb.length) {
            combs.add(Arrays.stream(comb).boxed().toList());
            return combs;
        }

        for (int i = start; i <= limit; i++) {
            comb[arrayIdx] = i;
            dfsRecursive(combs, comb, limit, i + 1, arrayIdx + 1);
        }
        return combs;
    }
}
