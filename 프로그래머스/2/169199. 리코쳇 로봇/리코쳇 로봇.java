import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(String[] board) {
        int answer = -1;
        int s_r = 0;
        int s_c = 0;
        int e_r = 0;
        int e_c = 0;
        int N = board.length;
        int M = board[0].length();
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i].charAt(j) == 'R') {
                    s_r = i;
                    s_c = j;
                } else if (board[i].charAt(j) == 'G') {
                    e_r = i;
                    e_c = j;
                }
            }
        }
        
        int[] dr = new int[] {-1, 1, 0, 0};
        int[] dc = new int[] {0, 0, -1, 1};
        
        boolean[][] visited = new boolean[N][M];
        visited[s_r][s_c] = true;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {s_r, s_c, 0});
        
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            if (cur[0] == e_r && cur[1] == e_c) {
                answer = cur[2];
                break;
            }
            
            for (int k = 0; k < 4; k++) {
                int nr = cur[0] + dr[k];
                int nc = cur[1] + dc[k];
                
                while (true) {
                    if (0 <= nr && nr < N && 0 <= nc && nc < M) {
                        if (board[nr].charAt(nc) != 'D') {
                            nr += dr[k];
                            nc += dc[k];
                        } else {
                            break;
                        }
                    } else {
                        break;
                    }
                }
                
                nr -= dr[k];
                nc -= dc[k];
                if (!visited[nr][nc]) {
                    visited[nr][nc] = true;
                    q.add(new int[] {nr, nc, cur[2]+1});
                }
                
            }
        }
        
        return answer;
    }
}