import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        for (int t = 0; t < 3; t++) {
            boolean[] dp = new boolean[100001];

            ArrayDeque<int[]> coins = new ArrayDeque<>();
            dp[0] = true;
            int sum = 0;
            int N = Integer.parseInt(br.readLine());
            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine(), " ");
                int coin = Integer.parseInt(st.nextToken());
                int cnt = Integer.parseInt(st.nextToken());
                sum += coin * cnt;
                for (int k = 1; k <= cnt; k++) {
                    dp[k * coin] = true;
                }
                coins.offer(new int[]{coin, cnt, sum});
            }
            if (sum % 2 == 1) sb.append(0).append("\n");
            else if (dp[sum/2]) sb.append(1).append("\n");
            else {
                while (!coins.isEmpty()) {
                    int[] now = coins.poll();
                    if (now[2] > 50000) now[2] = 50000;
                    for (int p = 0; p < now[1]; p++) {
                        for (int j = now[2]; j > now[0]; j--) {
                            if ((j - now[0]) % now[0] == 0 && (j - now[0]) <= now[0] * now[1]) continue;
                            dp[j] |= dp[j - now[0]];
                        }
                    }
                }
                if (dp[sum / 2]) sb.append(1).append("\n");
                else sb.append(0).append("\n");
                }
        }
        System.out.println(sb);
    }
}
