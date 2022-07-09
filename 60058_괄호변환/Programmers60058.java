public class Programmers60058 {
    public static void main(String args[]) {

    }
}

class Solution {
    private String[] splitBalanced(String w) {
        int leftCnt = 0;
        int rightCnt = 0;
        int splitIdx = 0;
        for (int i = 0; i < w.length(); i++) {
            if (w.charAt(i) == '(') {
                leftCnt++;
            } else {
                rightCnt++;
            }
            if (leftCnt == rightCnt) {
                splitIdx = i;
                break;
            }
        }
        return new String[]{w.substring(0, splitIdx + 1), w.substring(splitIdx + 1)};
    }

    private boolean isRightString(String u) {
        int leftCnt = 0;
        int rightCnt = 0;
        for (int i = 0; i < u.length(); i++) {
            if (u.charAt(i) == '(') leftCnt++;
            else rightCnt++;
            if (rightCnt > leftCnt) return false;
        }
        return leftCnt == rightCnt;
    }

    private String flip(String u) {
        StringBuilder flipU = new StringBuilder();
        for (int i = 0; i < u.length(); i++) {
            flipU.append(u.charAt(i) == '(' ? ')' : '(');
        }
        return new String(flipU);
    }

    private String change(String p) {
        if (p.isEmpty())
            return p;
        String[] uv = splitBalanced(p);
        if (isRightString(uv[0])) {
            return uv[0] + change(uv[1]);
        } else {
            String v = "(" + change(uv[1]) + ")";
            String u = flip(uv[0].substring(1, uv[0].length() - 1));
            return (v + u);
        }
    }

    public String solution(String p) {
        String answer = change(p);
        return answer;
    }
}