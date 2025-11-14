import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Long[] resistance = new Long[N];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            resistance[i] = Long.parseLong(st.nextToken());
        }

        Long[][] dp = new Long[N][2];
        dp[0][0] = 0L;
        dp[0][1] = resistance[0];

        for (int i = 1; i < N; i++) {
            dp[i][0] = dp[i-1][1];
            dp[i][1] = Math.min(dp[i-1][0], dp[i-1][1]) + resistance[i];
        }

        System.out.println(Math.min(dp[N-1][0], dp[N-1][1]));

    }
}
