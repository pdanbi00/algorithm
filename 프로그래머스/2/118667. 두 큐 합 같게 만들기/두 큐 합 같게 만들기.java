import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();
        long t1 = 0;
        long t2 = 0;
        int max = 0;
        for (int i = 0; i < queue1.length; i++) {
            q1.add(queue1[i]);
            max = Math.max(max, queue1[i]);
            t1 += queue1[i];
            q2.add(queue2[i]);
            t2 += queue2[i];
        }
        
        long total = t1 + t2;
        if (total % 2 == 1) {
            return -1;
        }
        if (max > total / 2) {
            return -1;
        }
        
        for (int cnt = 0; cnt <= 600000; cnt++) {
            if (t1 > t2) {
                int tmp = q1.poll();
                q2.add(tmp);
                t1 -= tmp;
                t2 += tmp;
            } else if (t1 < t2) {
                int tmp = q2.poll();
                q1.add(tmp);
                t2 -= tmp;
                t1 += tmp;
            } else {
                return answer;
            }
            answer++;
        }
        
        return -1;
    }
}