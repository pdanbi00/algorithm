import java.util.PriorityQueue;
class Solution {
    public int solution(int n, int k, int[] enemy) {
        int answer = 0;
        if (k >= enemy.length) {
            return enemy.length;
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 0; i < enemy.length; i++) {
            pq.offer(enemy[i]);
            if (pq.size() > k) {
                int tmp = pq.poll();
                if (n - tmp < 0) {
                    return i;
                }
                n -= tmp;
            }
        }
        return enemy.length;
    }
}