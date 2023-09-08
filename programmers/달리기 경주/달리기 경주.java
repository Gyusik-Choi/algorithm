import java.util.HashMap;

class Solution {

    public String[] solution(String[] players, String[] callings) {
        HashMap<String, Integer> raceName = new HashMap<>();
        HashMap<Integer, String> raceNum = new HashMap<>();

        for (int i = 0; i < players.length; i++) {
            raceName.put(players[i], i + 1);
            raceNum.put(i + 1, players[i]);
        }

        for (String call : callings) {
            // call 선수의 등수
            int curNum = raceName.get(call);
            // call 선수의 이름
            String curName = call;

            // call 선수 앞 선수의 등수
            // -> raceNum 으로 이름 찾기
            int prevNum = curNum - 1;
            // call 선수 앞 선수의 이름
            String prevName = raceNum.get(prevNum);

            // value 바꾸기
            // -> HashMap 둘 다 변경
            raceName.put(curName, prevNum);
            raceName.put(prevName, curNum);

            raceNum.put(curNum, prevName);
            raceNum.put(prevNum, curName);
        }

        String[] answer = new String[players.length];

        for (int i = 1; i <= players.length; i++) {
            answer[i - 1] = raceNum.get(i);
        }

        return answer;
    }
}
