import java.util.*;

class Solution {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(Arrays.toString(solution.solution(5, new int[]{2, 1, 2, 6, 2, 4, 3, 3})));
        System.out.println(Arrays.toString(solution.solution(4, new int[]{4, 4, 4, 4, 4})));
    }

    public int[] solution(int N, int[] stages) {
        HashMap<Integer, Integer> stageInfo = new HashMap<Integer, Integer>();

        for (int stage : stages) {
            if (stageInfo.containsKey(stage)) {
                stageInfo.put(stage, stageInfo.get(stage) + 1);
            } else {
                stageInfo.put(stage, 1);
            }
        }

        int total = stages.length;
        ArrayList<Stage> rate = new ArrayList<Stage>();

        for (int i = 1; i < N + 1; i++) {
            if (stageInfo.containsKey(i)) {
                int users = stageInfo.get(i);
                rate.add(new Stage(i, (double) users / total));
                total -= users;
            } else {
                rate.add(new Stage(i, 0.0));
            }
        }

        Collections.sort(rate);
        return rate.stream().mapToInt(r -> r.number).toArray();
    }

    static class Stage implements Comparable<Stage> {
        int number;
        double rate;

        Stage(int number, double rate) {
            this.number = number;
            this.rate = rate;
        }

        @Override
        public int compareTo(Stage s) {
            if (this.rate == s.rate) {
                return this.number - s.number;
            }

            return Double.compare(s.rate, this.rate);
        }
    }
}
