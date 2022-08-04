import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LeetCode_Medium676 {
    public static void main(String args[]){

         // Your MagicDictionary object will be instantiated and called as such:
        String[] dictionary = {"hello", "leetcode"};
        String[] searchWords = {"hello", "hhllo", "hell", "leetcoded"};
        MagicDictionary obj = new MagicDictionary();
        obj.buildDict(dictionary);

        for(int i=0;i<searchWords.length;i++)
            System.out.println(obj.search(searchWords[i]));

    }
}


class MagicDictionary {
    private Map<Integer, List<String>> lenBuckets;
    public MagicDictionary() {
        lenBuckets = new HashMap<Integer, List<String>>();
    }

    public void buildDict(String[] dictionary) {
        for(String s:dictionary){
            List<String> value = lenBuckets.get(s.length());
            if(value == null){
                value = new ArrayList<String>();
                lenBuckets.put(s.length(), value);
            }
            value.add(s);
        }
    }

    public boolean search(String searchWord) {
        List<String> bucket = lenBuckets.get(searchWord.length());
        if(bucket == null)
            return  false;

        for(String s:bucket){
            int diffCnt=0;
            for(int i=0;i<s.length();i++){
                if(s.charAt(i) != searchWord.charAt(i))
                    diffCnt++;
            }
            if(diffCnt == 1)
                return true;
        }
        return false;
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dictionary);
 * boolean param_2 = obj.search(searchWord);
 */