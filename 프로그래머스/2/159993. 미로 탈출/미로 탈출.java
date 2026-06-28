import java.util.*;
class Solution {
    public int solution(String[] maps) {
        int answer = 0;
        int N = maps.length;
        int M = maps[0].length();
        int sR, sC, eR, eC, lR, lC;
        sR = sC = eR = eC = lR = lC = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (maps[i].charAt(j) == 'S') {
                    sR = i;
                    sC = j;
                } else if (maps[i].charAt(j) == 'E') {
                    eR = i;
                    eC = j;
                } else if (maps[i].charAt(j) == 'L') {
                    lR = i;
                    lC = j;
                }
            }
        }
        
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};
        
        // start -> 레버
        Queue<Dot> q = new LinkedList<>();
        boolean[][] visited = new boolean[N][M];
        q.add(new Dot(sR, sC, 0));
        visited[sR][sC] = true;
        boolean possible = false;
        
        while (!q.isEmpty()) {
            Dot cur = q.poll();
            if (cur.r == lR && cur.c == lC) {
                answer += cur.cnt;
                possible = true;
                break;
            }
            for (int k = 0; k < 4; k++) {
                int nr = cur.r + dr[k];
                int nc = cur.c + dc[k];
                if (0 <= nr && nr < N && 0 <= nc && nc < M) {
                    if (maps[nr].charAt(nc) != 'X' && !visited[nr][nc]) {
                        q.add(new Dot(nr, nc, cur.cnt+1));
                        visited[nr][nc] = true;
                    } 
                }
            }
        }
        if (!possible) return -1;
            
        // 레버 -> exit
        q = new LinkedList<>();
        visited = new boolean[N][M];
        q.add(new Dot(lR, lC, 0));
        visited[lR][lC] = true;
        possible = false;
        
        while (!q.isEmpty()) {
            Dot cur = q.poll();
            if (cur.r == eR && cur.c == eC) {
                answer += cur.cnt;
                possible = true;
                break;
            }
            for (int k = 0; k < 4; k++) {
                int nr = cur.r + dr[k];
                int nc = cur.c + dc[k];
                if (0 <= nr && nr < N && 0 <= nc && nc < M) {
                    if (maps[nr].charAt(nc) != 'X' && !visited[nr][nc]) {
                        q.add(new Dot(nr, nc, cur.cnt+1));
                        visited[nr][nc] = true;
                    } 
                }
            }
        }
        if (!possible) return -1;
        
        return answer;
    }
    class Dot {
        int r, c, cnt;
        
        public Dot(int r, int c, int cnt) {
            this.r = r;
            this.c = c;
            this.cnt = cnt;
        }
    }
}