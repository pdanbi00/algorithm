import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int t : tangerine) {
            int tmp = map.getOrDefault(t, 0);
            map.put(t, tmp+1);
        }
        List<Integer> valueList = new ArrayList<>(map.values());
        valueList.sort(Collections.reverseOrder());
        for (int t : valueList) {
            k -= t;
            answer++;
            if (k <= 0) {
                break;
            }
        }
        
        return answer;
    }
}