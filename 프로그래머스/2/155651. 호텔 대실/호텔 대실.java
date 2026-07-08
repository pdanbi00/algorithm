import java.util.*;
class Solution {
    public int solution(String[][] book_time) {
        int answer = 0;
        Arrays.sort(book_time, (o1, o2) -> o1[0].compareTo(o2[0]));
        int N = book_time.length;
        int[][] newTime = new int[N][2];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < 2; j++) {
                int time = 0;
                String[] tmp = book_time[i][j].split(":");
                time += Integer.parseInt(tmp[0]) * 60;
                time += Integer.parseInt(tmp[1]);
                newTime[i][j] = time;
            }
        }
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 0; i < N; i++) {
            if (!pq.isEmpty()) {
                int tmp = pq.poll();
                if (newTime[i][0] < tmp + 10) {
                    pq.offer(tmp);
                }
            }
            pq.offer(newTime[i][1]);
            answer = Math.max(answer, pq.size());
        }
        
        return answer;
    }
}