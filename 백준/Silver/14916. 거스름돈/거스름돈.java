import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[100001];

        dp[2] = 1;
        dp[4] = 2;
        dp[5] = 1;

        for (int i = 6; i <= n; i++) {
            if (i-2 >= 0 && dp[i-2] > 0) {
                dp[i] = dp[i-2] + 1;
            }

            if (i-5 >= 0 && dp[i-5] > 0) {
                dp[i] = Math.min(dp[i], dp[i-5] + 1);
            }
        }

        if (dp[n] == 0) {
            System.out.println(-1);
        } else {
            System.out.println(dp[n]);
        }
    }
}
