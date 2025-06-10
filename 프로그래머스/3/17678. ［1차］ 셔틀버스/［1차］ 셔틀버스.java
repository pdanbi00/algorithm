import java.util.*;
class Solution {
    public String solution(int n, int t, int m, String[] timetable) {
        String answer = "";
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (String tt : timetable) {
            int time = Integer.parseInt(tt.substring(0, 2)) * 60 + Integer.parseInt(tt.substring(3));
            pq.add(time);
        }
        int now = 9 * 60; // 현재 시간
        int last = 0; // 마지막 시간
        int total = 0; // 셔틀버스 탑승 인원
        for (int i = 0; i < n; i++) {
            total = 0;
            while (!pq.isEmpty()) {
                int cur = pq.peek();
                // 버스 출발 시간보다 일찍 오고, 버스 인원이 남아있다면
                if (cur <= now && total < m) {
                    pq.poll();
                    total++;
                } else {
                    break;
                }
                last = cur;
            }
            now += t;
            
        }
        // 마지막 셔틀에 탄 인원이 m명보다 작으면 해당 셔틀 도착시간에 탈 수 있음.
        if (total < m) {
            last = now - t;
        } else {
            last--; // 실제로 가장 마지막에 탄 인원의 시간을 저장해뒀기 때문에 그 사람보다 1분 빨라야 탈 수 있음.
        }
        
        String hour = String.format("%02d", last / 60);
        String minute = String.format("%02d", last % 60);
        return hour + ":" + minute;
    }
}