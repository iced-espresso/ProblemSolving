import java.util.Collections;
import java.util.PriorityQueue;

public class LeetCode_Medium767 {
    static public void main(String args[]){
        String s = "aab";
        System.out.println(new Solution().reorganizeString(s));

        s = "aaab";
        System.out.println(new Solution().reorganizeString(s));

    }
}

class Solution {
    int[] count = new int[256];

    private char getMaxCntAlphabet(char except){
        char maxc = '-';
        for(char c='a'; c<='z'; c++){
            if(except == c)
                continue;
            if(count[c] > count[maxc])
                maxc = c;
        }
        return maxc;
    }
public String reorganizeString(String s) {
        for(int i=0;i<s.length();i++){
        count[s.charAt(i)]++;
        }
        StringBuilder stringBuilder = new StringBuilder();

        char c = '-';
        for (int i=0;i<s.length();i++) {
        c = getMaxCntAlphabet(c);
        if(c == '-')
        return "";
        stringBuilder.append(c);
        count[c]--;
        }

        return stringBuilder.toString();
        }
}

//
//class Solution {
//
//    class Node implements Comparable<Node>{
//        char c;
//        int count;
//        public Node(char c, int count){
//            this.c=c;
//            this.count=count;
//        }
//
//        @Override
//        public int compareTo(Node target){
//            return Integer.compare(this.count, target.count);
//        }
//    }
//    Node[] nodes = new Node[28];
//    PriorityQueue<Node> priorityQueue;
//    private char getMaxCntAlphabet(char except){
//        Node maxNode = priorityQueue.poll();
//        if(maxNode.c == except){
//            if(priorityQueue.isEmpty())
//                return '-';
//            Node temp = maxNode;
//            maxNode = priorityQueue.poll();
//            priorityQueue.add(temp);
//        }
//
//        if(maxNode.count <= 0)
//            return '-';
//
//        maxNode.count--;
//        priorityQueue.add(maxNode);
//        return maxNode.c;
//    }
//    public String reorganizeString(String s) {
//        priorityQueue = new PriorityQueue<>(Collections.reverseOrder());
//
//        for(char c='a'; c<='z'; c++){
//            nodes[c-'a'] = new Node(c,0);
//        }
//
//        for(int i=0;i<s.length();i++){
//            nodes[s.charAt(i)-'a'].count++;
//        }
//
//        for(char c='a'; c<='z'; c++){
//            priorityQueue.add(nodes[c-'a']);
//        }
//
//        StringBuilder stringBuilder = new StringBuilder();
//
//        char c = '-';
//        for (int i=0;i<s.length();i++) {
//
//            c = getMaxCntAlphabet(c);
//            if(c == '-')
//                return "";
//            stringBuilder.append(c);
//        }
//
//        return stringBuilder.toString();
//    }
//}
