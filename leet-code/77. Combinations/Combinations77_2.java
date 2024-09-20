import java.util.ArrayList;
import java.util.List;

public class Combinations77_2 {
    public List<List<Integer>> combine(int n, int k) {
        return dfsRecursive(new ArrayList<>(), new ArrayList<>(), 1, n, k);
    }

    private List<List<Integer>> dfsRecursive(List<List<Integer>> combs, List<Integer> comb, int start, int end, int size) {
        if (comb.size() == size) {
            combs.add(new ArrayList<>(comb));
            return combs;
        }

        for (int n = start; n <= end; n++) {
            comb.add(n);
            dfsRecursive(combs, comb, n + 1, end, size);
            comb.remove(comb.size() - 1);
        }
        return combs;
    }
}
