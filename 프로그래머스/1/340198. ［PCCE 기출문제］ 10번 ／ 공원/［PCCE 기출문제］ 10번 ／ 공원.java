class Solution {
    public int solution(int[] mats, String[][] park) {
        int answer = -1;
        int N = park.length;
        int M = park[0].length;
        int tmp = 0;
        
        int[][] board = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (park[i][j].equals("-1")) {
                    board[i][j] = 1;
                } else {
                    board[i][j] = 0;
                }
            }
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == 1) {
                    if (i - 1 >= 0 && j - 1 >= 0) {
                        int plus = Math.min(board[i-1][j], board[i][j-1]);
                        plus = Math.min(plus, board[i-1][j-1]);
                        board[i][j] += plus;
                        tmp = Math.max(tmp, board[i][j]);
                    }
                }
            }
        }
        
        for (int mat : mats) {
            if (mat <= tmp) {
                answer = Math.max(answer, mat);
            }
        }
        return answer;
    }
}