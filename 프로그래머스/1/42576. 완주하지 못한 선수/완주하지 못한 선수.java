import java.util.*;
class Solution {
    public String solution(String[] participants, String[] completion) {
        String answer = "";
        Map<String, Integer> name = new HashMap<>();
        for (String participant : participants) {
            name.put(participant, name.getOrDefault(participant, 0) + 1);
        }
        for (String comple : completion) {
            name.put(comple, name.getOrDefault(comple, 0) + 1);
        }
        
        for (Map.Entry<String, Integer> entry : name.entrySet()) {
            String key = entry.getKey();
            Integer value = entry.getValue();
            if (value % 2 == 1) {
                return key;
            }
        }
        return answer;
    }
}