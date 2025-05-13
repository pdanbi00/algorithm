import java.util.*;
class Solution {
    public String[] solution(String myString) {
        String[] answer = myString.split("x");
        List<String> list = new ArrayList<>();
        
        for (String str : answer) {
            if (!str.isEmpty()) {
                list.add(str);
            }
        }
        
        String[] result = new String[list.size()];
        list.toArray(result);
        Arrays.sort(result);
        
        return result;
    }
}