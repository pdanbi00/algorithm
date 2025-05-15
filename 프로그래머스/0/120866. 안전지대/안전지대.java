class Solution {
    public int solution(int[][] board) {
        int answer = 0;
        int n = board.length;
        int[][] visited = new int[n][n];
        int[] dr = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dc = {-1, 0, 1, -1, 1, -1, 0, 1};
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 1) {
                    visited[i][j] += 1;
                    for (int k = 0; k < 8; k++) {
                        int nr = i + dr[k];
                        int nc = j + dc[k];
                        if (0 <= nr && nr < n && 0 <= nc && nc < n) {
                            visited[nr][nc] += 1;
                        }
                    }
                }
            }
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j] == 0) {
                    answer++;
                }
            }
        }
        return answer;
    }
}