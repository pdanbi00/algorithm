import java.util.*;
class Solution {
    public int[] solution(int[][] score) {
        int[] answer = new int[score.length];
        List<Integer> scoreList = new ArrayList<>();
        for (int i = 0; i < score.length; i++) {
            scoreList.add(score[i][0] + score[i][1]);
        }
        for (int i = 0; i < score.length; i++) {
            int idx = 1;
            for (int j = 0; j < score.length; j++) {
                if (scoreList.get(i) < scoreList.get(j)) {
                    idx++;
                }
            }
            answer[i] = idx;
        }
        return answer;
    }
}