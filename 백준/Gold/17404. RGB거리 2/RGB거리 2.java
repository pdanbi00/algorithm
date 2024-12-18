import java.util.*;
import java.io.*;

public class Main {
    static final int INF = 1000*1000 + 1;

    static int N;
    static int[][] rgb, dp;
    static int answer = INF;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 입력받기
        N = Integer.parseInt(br.readLine());
        rgb = new int[N+1][3];
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < 3; j++) {
                rgb[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dp = new int[N+1][3];
        for (int k = 0; k < 3; k++) {
            // 초기화 : 첫번째 줄의 i번째 집 색칠
            for (int i = 0; i < 3; i++) {
                if (i == k) {
                    dp[1][i] = rgb[1][i];
                } else {
                    dp[1][i] = INF;
                }
            }

            // 2번째 집부터 채우기
            for (int i = 2; i <= N; i++) {
                dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2]) + rgb[i][0];
                dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2]) + rgb[i][1];
                dp[i][2] = Math.min(dp[i-1][0], dp[i-1][1]) + rgb[i][2];
            }

            // 정답 구하기
            for (int i = 0; i < 3; i++) {
                if (i != k) {
                    answer = Math.min(answer, dp[N][i]);
                }
            }
        }

        System.out.println(answer);
    }
}
