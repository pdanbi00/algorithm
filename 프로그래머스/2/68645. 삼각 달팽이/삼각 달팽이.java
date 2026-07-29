import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    public int[] solution(int n) {
        int[] answer = {};
        int num = 1;
        int total = 0;
        int[][] board = new int[n][n];
        for (int i = 1; i <= n; i++) {
            total += i;
        }
        
        int lap = 0;
        while (num <= total) {
            // 아래로 내려가기
            for (int i = lap * 2; i < n-lap; i++) {
                board[i][lap] = num;
                num++;
                if (num > total) break;
            }
            if (num > total) break;
            
            // 마지막행 다 채우기
            int idx = lap+1;
            while ((idx < n) && board[n-(lap+1)][idx] == 0) {
                board[n-(lap+1)][idx] = num;
                num++;
                idx++;
                if (num > total) break;
            }
            if (num > total) break;
            
            // 올라가기
            for (int i = n-(lap+2); i > lap*2; i--) {
                board[i][i-lap] = num;
                num++;
                if (num > total) break;
            }
            if (num > total) break;
            
            lap++;
        }
        
        ArrayList<Integer> tmp = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] != 0) {
                    tmp.add(board[i][j]);
                }
            }
        }
        answer = new int[tmp.size()];
        for (int i = 0; i < tmp.size(); i++) {
            answer[i] = tmp.get(i);
        }
        
        return answer;
    }
}