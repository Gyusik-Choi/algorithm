import java.util.ArrayList;
import java.util.List;

public class Permutations46 {
    public List<List<Integer>> permute(int[] nums) {
         return getPermutations(nums, new ArrayList<>(), new ArrayList<>());
    }

    private List<List<Integer>> getPermutations(int[] num, List<List<Integer>> perms, List<Integer> perm) {
        if (num.length == perm.size()) {
            perms.add(new ArrayList<>(perm));
            return perms;
        }

         for (int n : num) {
             if (!perm.contains(n)) {
                 perm.add(n);
                 getPermutations(num, perms, perm);
                 perm.remove(perm.size() - 1);
             }
         }
         return perms;
    }
}
