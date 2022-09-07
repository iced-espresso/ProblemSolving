public class Programmers17681 {
    public static void main(String args[]){
        System.out.println(new Solution()
                .solution(5, new int[]{9, 20, 28, 18, 11}, new int[]{30, 1, 21, 17, 28}));
    }
}

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        for (int i = 0; i < n; i++) {
            String bin = Integer.toBinaryString(arr1[i] | arr2[i]);
            bin = (new String(new char[n-bin.length()]).replace("\0", "0")) + bin;
            answer[i] = bin.replace("1", "#").replace("0", " ");
        }
        return answer;
    }
}
