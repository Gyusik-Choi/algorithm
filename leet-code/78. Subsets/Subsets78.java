import java.util.ArrayList;
import java.util.List;

public class Subsets78 {
    public List<List<Integer>> subsets(int[] nums) {
        return dfs(new ArrayList<>(), new ArrayList<>(), nums, 0);
    }

    private List<List<Integer>> dfs(List<List<Integer>> subsets, List<Integer> subset, int[] nums, int idx) {
        subsets.add(new ArrayList<>(subset));
        for (int i = idx; i < nums.length; i++) {
            subset.add(nums[i]);
            dfs(subsets, subset, nums, i + 1);
            subset.remove(subset.size() - 1);
        }
        return subsets;
    }
}
