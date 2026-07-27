import java.util.*;
class Solution {
    public int solution(int[][] scores) {
        int answer = 1;
        int[] wonho = scores[0];
        
        Arrays.sort(scores, (o1, o2) -> o1[0] == o2[0] ? o1[1] - o2[1] : o2[0] - o1[0]);
        int max = 0;
        
        for (int i = 0; i < scores.length; i++) {
            if (scores[i][0] > wonho[0] && scores[i][1] > wonho[1]) {
                return -1;
            }
            if (scores[i][1] >= max) {
                if (scores[i][0] + scores[i][1] > wonho[0] + wonho[1]) answer++;
                max = Math.max(max, scores[i][1]);
            }
            
        }
        return answer;
    }
}