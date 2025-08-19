import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long[] dp = new long[5001];

        dp[0] = 1;
        for (int n = 2; n < 5001; n += 2) {
            for (int i = 2; i <= n; i += 2) {
                dp[n] += dp[i-2] * dp[n-i];
                dp[n] %= 1000000007;
            }

        }

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            int L = Integer.parseInt(br.readLine());
            System.out.println(dp[L]);
        }
    }
}
