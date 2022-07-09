import java.sql.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class Programmers64065 {
    public static void main(String args[]){
        Solution solution = new Solution();
        int[] answer = solution.solution("{{1,2,3},{2,1},{1,2,4,3},{2}}");
        System.out.println(answer);
    }
}

class Solution {
    public int[] solution(String s) {
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        ArrayList<Integer> answer = new ArrayList<Integer>();
        s = s.substring(2,s.length()-2);
        String[] splited = s.split("},[{]");
        Arrays.sort(splited, (String s1, String s2) -> s1.length() - s2.length());
        for(String ss:splited){
            String[] x = ss.split(",");
            for(String y:x){
                if(!map.containsKey(y)){
                    map.put(y,1);
                    answer.add(Integer.parseInt(y));
                }
            }

        }
        return answer.stream().mapToInt(i->i).toArray();
    }
}