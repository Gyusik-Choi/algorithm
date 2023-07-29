import java.util.ArrayDeque;

class Solution {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution("(()())()"));
        System.out.println(solution.solution(")("));
        System.out.println(solution.solution("()))((()"));
    }

    public String solution(String p) {
        if (p.isEmpty()) {
            return p;
        }

        String[] pArr = splitP(p);
        String u = pArr[0];
        String v = pArr[1];

        if (isRightString(u)) {
            return u + solution(v);
        }

        String words = "(";
        words += solution(v);
        words += ")";
        u = u.substring(1);
        u = u.substring(0, u.length() - 1);
        u = changeDirection(u);
        return words + u;
    }

    public String[] splitP(String p) {
        int leftPair = 0;
        int rightPair = 0;
        StringBuilder u = new StringBuilder(p.substring(0, 1));
        String v = "";
        p = p.substring(1);

        if (u.toString().equals("(")) {
            leftPair += 1;
        } else {
            rightPair += 1;
        }

        for (int i = 0; i < p.length(); i++) {
            String str = p.substring(i, i + 1);

            if (str.equals("(")) {
                leftPair += 1;
            } else {
                rightPair += 1;
            }

            u.append(str);

            if (leftPair == rightPair) {
                if (leftPair != p.length()) {
                    v = p.substring(i + 1);
                }
                break;
            }
        }

        return new String[]{u.toString(), v};
    }

    public boolean isRightString(String u) {
        ArrayDeque<String> deq = new ArrayDeque<>();

        for (int i = 0; i < u.length(); i++) {
            String str = u.substring(i, i + 1);

            if (str.equals("(")) {
                deq.add(str);
            } else {
                if (deq.isEmpty()) {
                    return false;
                }

                deq.pollLast();
            }
        }

        return deq.isEmpty();
    }

    public String changeDirection(String u) {
        StringBuilder newU = new StringBuilder();

        for (int i = 0; i < u.length(); i++) {
            String str = u.substring(i, i + 1);

            if (str.equals("(")) {
                newU.append(")");
            } else {
                newU.append("(");
            }
        }

        return newU.toString();
    }
}
