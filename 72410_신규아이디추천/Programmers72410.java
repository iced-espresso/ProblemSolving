public class Programmers72410 {

    public static void main(String[] args) {
        String test = "z-+.^.";
        Solution sol = new Solution();
        sol.solution("...!@BaT#*..y.abcdefghijklm");
        sol.solution(test);
        sol.solution("=.=");
        sol.solution("123_.def");
    }
}

class Solution {

    public String solution(String new_id) {
        return new NewId(new_id).makeNewId().toString();
    }
}

class NewId {
    private String id;

    public NewId(String _id) {
        this.id = _id;
    }

    private NewId runStep1() {
        return new NewId(id.toLowerCase());
    }

    private NewId runStep2() {
        return new NewId(id.replaceAll("[^-_.a-z0-9]+", ""));
    }

    private NewId runStep3() {
        return new NewId(id.replaceAll("\\.{2,}", "."));
    }

    private NewId runStep4() {
        String newId = id;
        newId = newId.replaceAll("^\\.", "");
        newId = newId.replaceAll("[.]$", "");
        return new NewId(newId);
    }

    private NewId runStep5() {
        if (id.isEmpty()) {
            return new NewId("a");
        }
        return this;
    }

    private NewId runStep6() {
        String newId = id;
        if (newId.length() >= 16) {
            newId = newId.substring(0, 15);
            newId = newId.replaceAll("[.]$", "");
        }
        return new NewId(newId);
    }

    private NewId runStep7() {
        StringBuilder stringBuilder = new StringBuilder(id);
        char lastChar = stringBuilder.charAt(stringBuilder.length() - 1);
        while (stringBuilder.length() <= 2) {
            stringBuilder.append(lastChar);
        }
        return new NewId(stringBuilder.toString());
    }

    public NewId makeNewId() {
            return this
                .runStep1()
                .runStep2()
                .runStep3()
                .runStep4()
                .runStep5()
                .runStep6()
                .runStep7();
    }

    @Override
    public String toString() {
        return id;
    }
}