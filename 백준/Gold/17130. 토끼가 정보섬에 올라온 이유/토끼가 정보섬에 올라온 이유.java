import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int rR = 0, rC = 0;

        char[][] board = new char[N][M];
        int[][] dp = new int[N][M];
        for (int i = 0; i < N; i++) {
            String arr = br.readLine();
            for (int j = 0; j < M; j++) {
                dp[i][j] = -1;
                board[i][j] = arr.charAt(j);
                if (board[i][j] == 'R') {
                    rR = i;
                    rC = j;
                    dp[rR][rC] = 0;
                }
            }
        }

        int[] dr = new int[] {-1, 0, 1};
        int[] dc = new int[] {-1, -1, -1};

        boolean possible = false;
        int nr, nc;
        int answer = 0;

        for (int c = rC; c < M; c++) {
            for (int r = 0; r < N; r++) {
                if (board[r][c] == '#') {
                    continue;
                }

                for (int k = 0; k < 3; k++) {
                    nr = r + dr[k];
                    nc = c + dc[k];
                    if (nr >= 0 && nr < N && nc >= 0 && nc < M) {
                        if (dp[nr][nc] != -1) {
                            if (board[r][c] =='C') {
                                dp[r][c] = Math.max(dp[r][c], dp[nr][nc] + 1);
                            } else if (board[r][c] == '.') {
                                dp[r][c] = Math.max(dp[r][c], dp[nr][nc]);
                            } else if (board[r][c] == 'O') {
                                possible = true;
                                dp[r][c] = Math.max(dp[r][c], dp[nr][nc]);
                                answer = Math.max(answer, dp[r][c]);
                            }
                        }
                    }
                }
            }
        }
        if (possible) {
            System.out.println(answer);
        } else {
            System.out.println(-1);
        }
    }
}
