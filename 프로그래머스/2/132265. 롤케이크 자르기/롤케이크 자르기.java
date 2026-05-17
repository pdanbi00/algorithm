import java.util.Map;
import java.util.HashMap;
class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        Map<Integer, Integer> bro_1 = new HashMap<>();
        Map<Integer, Integer> bro_2 = new HashMap<>();
        
        for (int e : topping) {
            bro_2.put(e, bro_2.getOrDefault(e, 0) + 1);
        }
        
        for (int e : topping) {
            bro_1.put(e, bro_1.getOrDefault(e, 0) + 1);
            
            if (bro_2.get(e) - 1 == 0) {
                bro_2.remove(e);
            } else {
                bro_2.put(e, bro_2.get(e) - 1);
            }
            
            if (bro_1.size() == bro_2.size()) {
                answer++;
            }
        }
        return answer;
    }
}