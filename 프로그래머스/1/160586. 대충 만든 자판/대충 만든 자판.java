import java.util.Map;
import java.util.HashMap;
class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int N = targets.length;
        int[] answer = new int[N];
        Map<Character, Integer> map = new HashMap<>();
        for (String key : keymap) {
            for (int i = 0; i < key.length(); i++) {
                map.put(key.charAt(i), Math.min(map.getOrDefault(key.charAt(i), i+1), i+1));
            }
        }
        for (int i = 0; i < targets.length; i++) {
            String target = targets[i];
            int cnt = 0;
            for (int j = 0; j < target.length(); j++) {
                if (!map.containsKey(target.charAt(j))) {
                    cnt = -1;
                    break;
                }
                cnt += map.get(target.charAt(j));
            }
            answer[i] = cnt;
        }
        return answer;
    }
}