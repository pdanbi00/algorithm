import java.util.*;
class Solution {
    public long solution(int[] weights) {
        long answer = 0;
        
        Map<Double, Integer> weightCount = new HashMap<>();
        Set<Double> weightSet = new HashSet();
        
        for (int w : weights) {
            weightCount.put(w * 1.0, weightCount.getOrDefault(w * 1.0, 0) + 1);
            weightSet.add(w * 1.0);
        }
        
        for (Double w : weightSet) {
            if (weightCount.get(w) >= 2) {
                answer +=  ((long) weightCount.get(w) * (long) (weightCount.get(w) - 1)) / 2;
            }
            
            if (weightCount.containsKey(w * 3 / 2)) {
                answer += (long) weightCount.get(w*3/2) * (long) weightCount.get(w);
            }
            if (weightCount.containsKey(w * 4 / 2)) {
                answer += (long) weightCount.get(w*4/2) * (long) weightCount.get(w);
            }
            if (weightCount.containsKey(w * 4 / 3)) {
                answer += (long) weightCount.get(w*4/3) * (long) weightCount.get(w);
            }
        }
 
        return answer;
    }
}