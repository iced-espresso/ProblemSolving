public class main {

    public static void main(String[] args)
    {
        String test = "z-+.^.";
        Solution sol = new Solution();
        sol.solution("...!@BaT#*..y.abcdefghijklm");
        sol.solution(test);
        sol.solution("=.=");
        sol.solution("123_.def");
    }
}

class Solution {
    private String _ProcessLeve1(String id)
    {
        if(id.length() == 0)
            return id;
        return id.toLowerCase();
    }
    private String _ProcessLeve2(String id){
        if(id.length() == 0)
            return id;
        String ret = "";
        String ref = "0123456789abcdefghijklmnopqrstuvwxyz-_.";
        for (int i=0;i<id.length();i++)
        {
            char c = id.charAt(i);
            if(ref.indexOf(c) != -1)
            {
                ret += c;
            }
        }
        return ret;
    }
    private String _ProcessLeve3(String id){
        if(id.length() == 0)
            return id;
        while(id.indexOf("..") != -1)
        {
            id = id.replace("..", ".");
        }
        return id;
    }
    private String _ProcessLeve4(String id){
        if(id.length() == 0)
            return id;
        if(id.charAt(0) == '.'){
            id = id.substring(1,id.length());
        }
        if(id.length() == 0)
            return id;
        if(id.charAt(id.length()-1) == '.'){
            id = id.substring(0,id.length()-1);
        }
        return id;
    }
    private String _ProcessLeve5(String id){
        if(id == ""){
            id = "a";
        }
        return id;

    }
    private String _ProcessLeve6(String id){
        if(id.length() == 0)
            return id;
        if(id.length() >= 16){
            id = id.substring(0,15);
        }
        return id;
    }
    private String _ProcessLeve7(String id){
        if(id.length() == 0)
            return id;
        while (id.length() <= 2){
            id += id.charAt(id.length()-1);
        }
        return id;

    }
    public String solution(String new_id) {
        String answer = "";
        new_id = _ProcessLeve1(new_id);
        new_id = _ProcessLeve2(new_id);
        new_id = _ProcessLeve3(new_id);
        new_id = _ProcessLeve4(new_id);
        new_id = _ProcessLeve5(new_id);
        new_id = _ProcessLeve6(new_id);
        new_id = _ProcessLeve7(new_id);

        return answer;
    }
}