import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] arr = {3, 1, 2};
        System.out.println(solution.solution(arr, 5));
    }

    public int solution(int[] foodTimes, long k) {
        // long sums = Arrays.stream(foodTimes).sum();
        // stream 대신 for 문으로 바꿔서 통과할 수 있었다
        //
        // int 가 아닌 long 타입
        long sums = 0;

        for (int foodTime : foodTimes) {
            sums += foodTime;
        }

        if (sums <= k) {
            return -1;
        }

        Food[] foods = new Food[foodTimes.length];

        for (int i = 0; i < foodTimes.length; i++) {
            foods[i] = new Food(i, foodTimes[i]);
        }

        // 음식을 다 먹는데 필요한 시간 순서 정렬
        Arrays.sort(foods, (a, b) -> a.time - b.time);

        // int 가 아닌 long 타입
        long foodLength = foodTimes.length;
        int lastTime = 0;
        int idx = 0;

        while (k >= (long)(foods[idx].time - lastTime) * foodLength) {
            k -= (long)(foods[idx].time - lastTime) * foodLength;

            int sameCnt = getSameCnt(foods, foods[idx].time, idx);

            foodLength -= sameCnt;

            lastTime = foods[idx].time;

            idx += sameCnt;
        }

        // 인덱스 정렬
        Arrays.sort(foods, (a, b) -> a.idx - b.idx);

        int finalLastTime = lastTime;

        List<Food> filteredFoods = Arrays
                .stream(foods)
                .filter(food -> food.time > finalLastTime)
                .collect(Collectors.toList());

        int foodIdx = (int) (k % filteredFoods.size());
        return filteredFoods.get(foodIdx).idx + 1;
    }

    public int getSameCnt(Food[] foods, int value, int idx) {
        int cnt = 0;

        for (int i = idx; i < foods.length; i++) {
            if (foods[i].time > value) {
                break;
            }

            if (foods[i].time == value) {
                cnt += 1;
            }
        }

        return cnt;
    }

    public static class Food {
        int idx;
        int time;

        Food(int idx, int time) {
            this.idx = idx;
            this.time = time;
        }
    }
}

// 참고
// https://velog.io/@kimdukbae/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AC%B4%EC%A7%80%EC%9D%98-%EB%A8%B9%EB%B0%A9-%EB%9D%BC%EC%9D%B4%EB%B8%8C-Java
// https://moonsbeen.tistory.com/371
// https://programmer-chocho.tistory.com/71
// https://dev-note-97.tistory.com/248