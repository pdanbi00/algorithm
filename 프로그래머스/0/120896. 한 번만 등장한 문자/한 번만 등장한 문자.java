import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public String solution(String s) {
        String answer = "";
        ArrayList<Character> arr = new ArrayList<>();
        Map<Character, Integer> map = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++) {
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
        }
        
        for (Character c : map.keySet()) {
            if (map.get(c) == 1) {
                arr.add(c);
            }
        }
        Collections.sort(arr);
        for (int i = 0; i < arr.size(); i++) {
            answer += arr.get(i);
        }
        return answer;
    }
}