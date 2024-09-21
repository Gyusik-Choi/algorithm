import java.util.ArrayList;
import java.util.List;

public class CombinationSum39 {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        return dfs(candidates, target, new ArrayList<>(), new ArrayList<>(), 0);
    }

    private List<List<Integer>> dfs(int[] candidates, int target, List<List<Integer>> combs, List<Integer> comb, int idx) {
        int sums = getSumOfList(comb);

        if (sums == target) {
            combs.add(new ArrayList<>(comb));
            return combs;
        }

        if (sums > target) {
            return combs;
        }

        for (int i = idx; i < candidates.length; i++) {
            comb.add(candidates[i]);
            dfs(candidates, target, combs, comb, i);
            comb.remove(comb.size() - 1);
        }
        return combs;
    }

    private int getSumOfList(List<Integer> list) {
        return list.stream().mapToInt(l -> l).sum();
    }
}
