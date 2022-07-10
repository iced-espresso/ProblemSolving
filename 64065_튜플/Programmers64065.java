import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class Programmers64065 {
    public static void main(String args[]) {
        Solution solution = new Solution();
        int[] answer = solution.solution("{{1,2,3},{2,1},{1,2,4,3},{2}}");
        System.out.println(answer);
    }
}

class Tuple {
    private ArrayList<Integer> tupleList = new ArrayList<Integer>();
    private HashMap<Integer, Integer> tupleMap = new HashMap<Integer, Integer>();
    ;

    public Tuple() {

    }

    public Tuple(String tupleStr) {
        for (String element : tupleStr.split(",")) {
            this.addElement(Integer.parseInt(element));
        }
    }

    public void addElement(Integer element) {
        if (!tupleMap.containsKey(element)) {
            tupleMap.put(element, 1);
            tupleList.add(element);
        }
    }

    public void addTuple(Tuple otherTuple) {
        for (Integer otherElement : otherTuple.tupleList) {
            addElement(otherElement);
        }
    }

    public int[] toArray() {
        return tupleList.stream().mapToInt(i -> i).toArray();
    }

}

class Solution {
    public int[] solution(String s) {
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        Tuple answer = new Tuple();

        s = s.substring(2, s.length() - 2);
        String[] elements = s.split("},[{]");
        Arrays.sort(elements, (s1, s2) -> s1.length() - s2.length());

        for (String element : elements) {
            answer.addTuple(new Tuple(element));
        }
        return answer.toArray();
    }
}