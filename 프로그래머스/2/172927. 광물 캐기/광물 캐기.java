import java.util.PriorityQueue;
import java.util.Comparator;

class Solution {
    static class Mineral{
        int d, ir, s;

        public Mineral(int d, int ir, int s) {
            this.d = d;
            this.ir = ir;
            this.s = s;
        }
    }

    public int solution(int[] picks, String[] minerals) {
        int answer = 0;
        PriorityQueue<Mineral> pq = new PriorityQueue<>(
            (a, b) -> {
                if (a.d != b.d) {
                    return b.d - a.d;
                }
                
                if (a.ir != b.ir) {
                    return b.ir - a.ir;
                }
                return b.s - a.s;
            }
        );
        
        int total = 0;
        for (int i = 0; i < 3; i++) {
            total += 5 * picks[i];
        }
        int N = minerals.length;
        for (int i = 0; i < N; i += 5) {
            int d = 0;
            int ir = 0;
            int s = 0;
            
            for (int j = 0; j < 5; j++) {
                if (i + j >= N || i + j >= total) {
                    break;
                }
                
                if (minerals[i+j].equals("diamond")) {
                    d += 1;
                } else if (minerals[i+j].equals("iron")) {
                    ir += 1;
                } else {
                    s += 1;
                }
            }
            pq.offer(new Mineral(d, ir, s));
            
        }
        
        int tool = 0;
        while (!pq.isEmpty()) {
            Mineral tmp = pq.poll();
            
            while (tool < 3 && picks[tool] <= 0) {
                tool++;
            }
            
            if (tool >=3) {
                break;
            }
            if (tool == 0) {
                answer += tmp.d + tmp.ir + tmp.s;
            } else if (tool == 1) {
                answer += tmp.d * 5 + tmp.ir + tmp.s;
            } else if (tool == 2) {
                answer += tmp.d * 25 + tmp.ir * 5 + tmp.s;
            }
            
            picks[tool]--;
        }
        
        return answer;
    }
    
}
