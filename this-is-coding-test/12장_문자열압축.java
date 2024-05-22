import static java.lang.Math.min;

class Solution2 {
    public static void main(String[] args) {
        Solution2 solution = new Solution2();
        System.out.println(solution.solution("aabbaccc"));
        System.out.println(solution.solution("ababcdcdababcdcd"));
        System.out.println(solution.solution("abcabcdede"));
        System.out.println(solution.solution("abcabcabcabcdededededede"));
        System.out.println(solution.solution("xababcdcdababcdcd"));
    }

    public StringBuilder tempS = new StringBuilder();

    public int solution(String s) {
        int minLength = s.length();

        for (int i = 1; i <= s.length() / 2; i++) {
            // https://stackoverflow.com/questions/7168881/what-is-more-efficient-stringbuffer-new-or-delete0-sb-length
            tempS.setLength(0);
            String prev = s.substring(0, i);
            int cnt = 1;

            for (int j = i; j <= s.length(); j += i) {
                // 인덱스 범위 초과 방지
                int idx = min(i + j, s.length());
                String cur = s.substring(j, idx);

                if (prev.equals(cur)) {
                    cnt += 1;
                    continue;
                }

                addRestPrev(cnt, prev);
                prev = cur;
                cnt = 1;
            }

            addRestPrev(cnt, prev);
            minLength = min(minLength, tempS.length());
        }

        return minLength;
    }

    private void addRestPrev(int cnt, String prev) {
        if (cnt > 1) {
            tempS.append(cnt);
        }

        tempS.append(prev);
    }
}

// 참고
// https://velog.io/@ckr3453/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%95%95%EC%B6%95-Java
