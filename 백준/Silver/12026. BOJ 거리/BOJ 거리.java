import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String blocks = br.readLine();

        int[] dp = new int[N];
        dp[0] = 0;
        for (int i = 1; i < N; i++) {
            dp[i] = Integer.MAX_VALUE;
        }

        for (int i = 0; i < N; i++) {
            if (blocks.charAt(i) == 'B') {
                for (int j = i+1; j < N; j++) {
                    if (blocks.charAt(j) == 'O') {
                        int tmp = Integer.MAX_VALUE;
                        if (dp[i] != Integer.MAX_VALUE) {
                            tmp = dp[i] + (j - i) * (j - i);
                        }
                        dp[j] = Math.min(dp[j], tmp);
                    }
                }
            } else if (blocks.charAt(i) == 'O') {
                for (int j = i+1; j < N; j++) {
                    if (blocks.charAt(j) == 'J') {
                        int tmp = Integer.MAX_VALUE;
                        if (dp[i] != Integer.MAX_VALUE) {
                            tmp = dp[i] + (j - i) * (j - i);
                        }
                        dp[j] = Math.min(dp[j], tmp);
                    }
                }
            } else if (blocks.charAt(i) == 'J') {
                for (int j = i+1; j < N; j++) {
                    if (blocks.charAt(j) == 'B') {
                        int tmp = Integer.MAX_VALUE;
                        if (dp[i] != Integer.MAX_VALUE) {
                            tmp = dp[i] + (j - i) * (j - i);
                        }
                        dp[j] = Math.min(dp[j], tmp);
                    }
                }
            }
        }

        if (dp[N-1] == Integer.MAX_VALUE) {
            System.out.println(-1);
        } else {
            System.out.println(dp[N-1]);
        }
    }
}
