import java.util.ArrayList;
import java.util.PriorityQueue;

class Solution {
    public int[] solution(int k, int[] score) {
        ArrayList<Integer> tmp = new ArrayList<>();
        int[] answer = {};
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int N = score.length;
        
        for (int i = 0; i < N; i++) {
            pq.offer(score[i]);
            if (pq.size() > k) {
                pq.poll();
            }
            tmp.add(pq.peek());
        }
        answer = new int[tmp.size()];
        for (int i = 0; i < tmp.size(); i++) {
            answer[i] = tmp.get(i);
        }
        return answer;
    }
}