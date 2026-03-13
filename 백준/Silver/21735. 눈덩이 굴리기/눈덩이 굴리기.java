import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] yard = new int[N+1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            yard[i] = Integer.parseInt(st.nextToken());
        }

        int[][] dp = new int[M+1][N+1];
        for (int i = 0; i < M+1; i++) {
            Arrays.fill(dp[i], -1);
        }
        int answer = 1;
        dp[0][0] = 1;

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (dp[i][j] != -1) {
                    // 굴리기
                    dp[i+1][j+1] = Math.max(dp[i+1][j+1], dp[i][j] + yard[j+1]);
                    answer = Math.max(answer, dp[i+1][j+1]);
                    // 던지기
                    if (j + 2 <= N) {
                        dp[i+1][j+2] = Math.max(dp[i+1][j+2], dp[i][j] / 2 + yard[j+2]);
                        answer = Math.max(answer, dp[i+1][j+2]);
                    }
                }
            }
        }

        System.out.print(answer);
    }
}