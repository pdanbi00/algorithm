import java.util.StringTokenizer;
import java.io.*;
import java.util.Arrays;
public class Main {
    static int N;
    static int[] SVC;
    static int[][][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        SVC = new int[3];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            SVC[i] = Integer.parseInt(st.nextToken());
        }
        dp = new int[61][61][61];
        for (int i = 0; i < 61; i++) {
            for (int j = 0; j < 61; j++) {
                Arrays.fill(dp[i][j], -1);
            }
        }

        System.out.println(dfs(SVC[0], SVC[1], SVC[2]));
    }
    static int dfs(int a, int b, int c) {
        a = Math.max(a, 0);
        b = Math.max(b, 0);
        c = Math.max(c, 0);

        if (a == 0 && b == 0 && c == 0) {
            return 0;
        }

        if (dp[a][b][c] != -1) {
            return dp[a][b][c];
        }

        int result = 987654321;

        result = Math.min(result, dfs(a-9, b-3, c-1) + 1);
        result = Math.min(result, dfs(a-9, b-1, c-3) + 1);
        result = Math.min(result, dfs(a-3, b-9, c-1) + 1);
        result = Math.min(result, dfs(a-3, b-1, c-9) + 1);
        result = Math.min(result, dfs(a-1, b-9, c-3) + 1);
        result = Math.min(result, dfs(a-1, b-3, c-9) + 1);

        return dp[a][b][c] = result;
    }
}
