import java.util.ArrayList;
import java.util.Collections;
class Solution {
    public String solution(String s) {
        String answer = "";
        ArrayList<Character> tmp = new ArrayList<>();
        
        for (int i = 0; i < s.length(); i++) {
            tmp.add(s.charAt(i));
        }
        Collections.sort(tmp, Collections.reverseOrder());
        for (int i = 0; i < s.length(); i++) {
            answer += tmp.get(i);
        }
        return answer;
    }
}