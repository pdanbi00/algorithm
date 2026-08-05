import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Collections;

class Solution {
    public int[] solution(String[] maps) {
        ArrayList<Integer> arr = new ArrayList<>();
        int[] answer = {};
        int N = maps.length;
        int M = maps[0].length();
        boolean[][] visited = new boolean[N][M];
        int[] dr = new int[] {-1, 1, 0, 0};
        int[] dc = new int[] {0, 0, -1, 1};
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (maps[i].charAt(j) != 'X' && !visited[i][j]) {
                    Queue<int[]> q = new LinkedList<>();
                    int tmp = 0;
                    q.offer(new int[] {i, j});
                    visited[i][j] = true;
                    
                    while(!q.isEmpty()) {
                        int[] cur = q.poll();
                        tmp += maps[cur[0]].charAt(cur[1]) - '0';
                        for (int k = 0; k < 4; k++) {
                            int nr = cur[0] + dr[k];
                            int nc = cur[1] + dc[k];
                            
                            if (0 <= nr && nr < N && 0 <= nc && nc < M) {
                                if (maps[nr].charAt(nc) != 'X' && !visited[nr][nc]) {
                                    q.offer(new int[] {nr, nc});
                                    visited[nr][nc] = true;
                                }
                            }
                        }
                    }
                    arr.add(tmp);
                } 
            }
        }
        if (arr.isEmpty()) {
            answer = new int[] {-1};
        } else {
            Collections.sort(arr);
            answer = new int[arr.size()];
            for (int i = 0; i < arr.size(); i++) {
                answer[i] = arr.get(i);
            }
        }
        
        return answer;
    }
}