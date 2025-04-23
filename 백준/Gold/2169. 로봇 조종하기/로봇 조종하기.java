import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] board = new int[N][M];
        int[][] dp = new int[N][M];
        int[][] temp = new int[2][M];

        int ans = 0;
        int[] dr = {0, 1, 0};
        int[] dc = {-1, 0, 1};

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dp[0][0] = board[0][0];
        for (int j = 1; j < M; j++) {
            dp[0][j] = dp[0][j-1] + board[0][j];
        }

        for (int i = 1; i < N; i++) {
            // 왼쪽 & 위쪽
            temp[0][0] = dp[i-1][0] + board[i][0];
            for (int j = 1; j < M; j++) {
                temp[0][j] = Math.max(temp[0][j-1], dp[i-1][j]) + board[i][j];
            }

            // 오른쪽 & 위쪽
            temp[1][M-1] = dp[i-1][M-1] + board[i][M-1];
            for (int j = M-2; j >= 0; j--) {
                temp[1][j] = Math.max(temp[1][j+1], dp[i-1][j]) + board[i][j];
            }

            // 둘 중의 최댓값
            for (int j = 0; j < M; j++) {
                dp[i][j] = Math.max(temp[0][j], temp[1][j]);
            }
        }

        System.out.print(dp[N-1][M-1]);
    }
}
