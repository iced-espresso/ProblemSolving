import java.util.HashMap;
import java.util.Map;

public class Porgrammers118666 {
    public static void main(String args[]){
        System.out.println(new Solution()
                .solution(new String[]{"AN", "CF", "MJ", "RT", "NA"}, new int[]{5, 3, 2, 7, 5}));
    }
}



class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        Map<String, Integer> personalityScore = new HashMap<String, Integer>() {{
            put("RT", 0); put("CF", 0); put("JM", 0); put("AN", 0);
        }};

        for (int i = 0; i < survey.length; i++) {
            int score = 4 - choices[i];
            if(personalityScore.containsKey(survey[i])){
                personalityScore.put(survey[i], personalityScore.get(survey[i]) + score);
            }
            else{
                String reversedServey = new StringBuffer(survey[i]).reverse().toString();
                personalityScore.put(reversedServey, personalityScore.get(reversedServey) - score);
            }
        }

        for(Map.Entry<String, Integer> entry: personalityScore.entrySet()){
            answer += entry.getValue() >= 0 ? entry.getKey().charAt(0) : entry.getKey().charAt(1);
        }

        return answer;
    }
}