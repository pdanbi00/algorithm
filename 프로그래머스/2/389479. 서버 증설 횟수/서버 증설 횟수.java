import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        int N = players.length;
        Queue<Integer> q = new LinkedList<>();
        
        for (int i = 0; i < N; i++) {
            int need = players[i] / m;
            
            while (!q.isEmpty() && q.peek() <= i) {
                q.poll();
            }
            
            int current = q.size();
            if (current < need) {
                answer += need - current;
                for (int j = 0; j < need-current; j++) {
                    q.offer(i+k);
                }
            }
            
        }
        return answer;
    }
}