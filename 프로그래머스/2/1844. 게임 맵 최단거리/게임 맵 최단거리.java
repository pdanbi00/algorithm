import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        int N = maps.length;
        int M = maps[0].length;
        
        int[] dr = new int[] {-1, 1, 0, 0};
        int[] dc = new int[] {0, 0, -1, 1};
        
        boolean[][] visited = new boolean[N][M];
        Queue<Dot> q = new LinkedList<>();
        q.offer(new Dot(0, 0, 1));
        visited[0][0] = true;
        while (!q.isEmpty()) {
            Dot cur = q.poll();
            if (cur.r == N-1 && cur.c == M-1) {
                answer = cur.cnt;
                break;
            }
            
            for (int k = 0; k < 4; k++) {
                int nr = cur.r + dr[k];
                int nc = cur.c + dc[k];
                
                if (0 <= nr && nr < N && 0 <= nc && nc < M) {
                    if (maps[nr][nc] == 1 && !visited[nr][nc]) {
                        q.offer(new Dot(nr, nc, cur.cnt+1));
                        visited[nr][nc] = true;
                    }
                }
            }
        }
        if (answer == 0) return -1;
        
        return answer;
    }
}

class Dot {
    int r, c, cnt;
    Dot(int r, int c, int cnt) {
        this.r = r;
        this.c = c;
        this.cnt = cnt;
    }
}