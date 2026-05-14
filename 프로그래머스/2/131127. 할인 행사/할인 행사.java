import java.util.*;
class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        Map<String, Integer> map = new HashMap<>();
        int N = want.length;
        int M = discount.length;
        for (int i = 0; i < N; i++) {
            map.put(want[i], number[i]);
        }
        
        for (int i = 0; i < M-9; i++) {
            Map<String, Integer> tmp = new HashMap<>();
            boolean possible = true;
            for (int j = 0; j < 10; j++) {
                if (!map.containsKey(discount[i+j])) {
                    possible = false;
                    break;
                }
                
                tmp.put(discount[i+j], tmp.getOrDefault(discount[i+j], 0) + 1);
                if (tmp.get(discount[i+j]) > map.get(discount[i+j])) {
                    possible = false;
                    break;
                }
            }
            if (possible) {
                for (String key : map.keySet()) {
                    if (map.get(key) != tmp.get(key)) {
                        possible = false;
                        break;
                    }
                }
            }
            if (possible) answer++;
        }
        return answer;
    }
}