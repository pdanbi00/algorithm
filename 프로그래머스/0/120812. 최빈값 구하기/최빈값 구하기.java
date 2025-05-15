import java.util.*;
class Solution {
    public int solution(int[] array) {
        
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < array.length; i++) {
            map.put(array[i], map.getOrDefault(array[i], 0) + 1);
        }
        int maxCount = 0; // 가장 높은 빈도
        int answer = 0; // 가장 빈도가 높은 수
        
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int num = entry.getKey();
            int cnt = entry.getValue();
            
            if (cnt > maxCount) {
                maxCount = cnt;
                answer = num;
            } else if (cnt == maxCount) {
                answer = -1;
            }
        }
        
        return answer;
    }
}