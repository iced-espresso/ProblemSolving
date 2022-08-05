import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Programmers42586 {
    public static void main(String args[]){
        Solution solution = new Solution();
        int[] ret1 = solution.solution(new int[]{93, 30, 55}, new int[]{1, 30, 5});
        int[] ret2 = solution.solution(new int[]{95, 90, 99, 99, 80, 99}, new int[]{1, 1, 1, 1, 1, 1});
        System.out.println(Arrays.equals(ret1, new int[]{2,1}));
        System.out.println(Arrays.equals(ret2, new int[]{1,3,2}));
        System.out.println(Arrays.toString(ret1) + Arrays.toString(ret2));
    }
}

class Solution {
    private int calCompleteDay(int progress, int speed){
        return (int) Math.ceil((double)(100-progress)/speed);
    }
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();

        int refDay = calCompleteDay(progresses[0], speeds[0]);
        int releaseCnt = 1;

        for(int i=1;i<progresses.length;i++){
            int completeDay = calCompleteDay(progresses[i], speeds[i]);
            if(completeDay <= refDay){
                releaseCnt++;
            }
            else{
                answer.add(releaseCnt);
                releaseCnt=1;
                refDay = completeDay;
            }
        }

        answer.add(releaseCnt);
        return answer.stream().mapToInt(i->i).toArray();
    }
}