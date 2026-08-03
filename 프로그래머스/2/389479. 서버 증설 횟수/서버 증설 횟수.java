import java.util.ArrayList;
import java.util.PriorityQueue;

class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        int N = players.length;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for (int i = 0; i < N; i++) {
            int user = players[i];
            int cnt = pq.size();
            if (user >= (cnt+1) * m) {
                int need = user / m;
                
                answer += need - cnt;
                for (int j = 0; j < need-cnt; j++) {
                    pq.offer(k);
                }
            }
            
            ArrayList<Integer> tmp = new ArrayList<>();
            while (!pq.isEmpty()) {
                int cur = pq.poll();
                if (cur - 1 <= 0) {
                    continue;
                }
                tmp.add(cur-1);
            }
            
            for (int j = 0; j < tmp.size(); j++) {
                pq.offer(tmp.get(j));
            }
            
        }
        return answer;
    }
}