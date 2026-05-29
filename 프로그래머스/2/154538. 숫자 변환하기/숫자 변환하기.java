import java.util.Queue;
import java.util.LinkedList;
class Solution {
    public int solution(int x, int y, int n) {
        int answer = 1000001;
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[] {y, 0});
        while (!q.isEmpty()) {
            int[] tmp = q.poll();
            
            if (tmp[0] == x) {
                answer = Math.min(answer, tmp[1]);
                break;
            }
            
            if (tmp[0] % 3 == 0) {
                q.offer(new int[] {tmp[0] / 3, tmp[1] + 1});
            }
            
            if (tmp[0] % 2 == 0) {
                q.offer(new int[] {tmp[0] / 2, tmp[1] + 1});
            }
            
            if (tmp[0] - n >= 0) {
                q.offer(new int[] {tmp[0] - n, tmp[1] + 1});
            }
        }
        
        if (answer == 1000001) {
            answer = -1;
        }
        return answer;
    }
}