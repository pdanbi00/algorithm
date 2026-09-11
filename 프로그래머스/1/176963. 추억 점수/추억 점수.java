import java.util.Map;
import java.util.HashMap;
class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        Map<String, Integer> map = new HashMap<>();
        int N = name.length;
        for (int i = 0; i < N; i++) {
            map.put(name[i], yearning[i]);
        }
        
        for (int i = 0; i < photo.length; i++) {
            int total = 0;
            for (int j = 0; j < photo[i].length; j++) {
                total += map.getOrDefault(photo[i][j], 0);
            }
            answer[i] = total;
        }
        
        return answer;
    }
}