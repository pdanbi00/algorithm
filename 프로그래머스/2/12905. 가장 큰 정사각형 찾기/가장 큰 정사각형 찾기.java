class Solution
{
    public int solution(int [][]board)
    {
        int N = board.length;
        int M = board[0].length;
        
        int answer = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] != 0) {
                    if (answer == 0) answer = 1;
                    if (i - 1 >= 0 && j - 1 >= 0) {
                        int tmp = Math.min(board[i-1][j-1], board[i-1][j]);
                        tmp = Math.min(tmp, board[i][j-1]);
                        board[i][j] += tmp;
                        answer = Math.max(answer, board[i][j]);
                    }
                }
                
            }
        }
        // for (int i = 0; i < N; i++) {
        //     for (int j = 0; j < M; j++) {
        //         System.out.print(board[i][j] + " ");
        //     }
        //     System.out.println();
        // }

        return answer * answer;
    }
}