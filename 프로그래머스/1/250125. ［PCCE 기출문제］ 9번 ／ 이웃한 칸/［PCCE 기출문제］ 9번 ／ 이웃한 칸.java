class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};
        
        int N = board.length;
        int M = board[0].length;
        String target = board[h][w];
        
        for (int k = 0; k < 4; k++) {
            int nr = h + dr[k];
            int nc = w + dc[k];
            
            if (nr < 0 || nr >= N || nc < 0 || nc >= M) {
                continue;
            }
            if (board[nr][nc].equals(target)){
                answer++;
            }
        }
        return answer;
    }
}