import java.io.*;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] trains = new int[N+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i < N+1; i++) {
            trains[i] = Integer.parseInt(st.nextToken());
            trains[i] += trains[i-1];
        }

        int M = Integer.parseInt(br.readLine());

        int[][] dp = new int[4][N+1];

        for (int i = 1; i < 4; i++) {
            for (int j = M * i; j < N+1; j++) {
                dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j-M] + trains[j] - trains[j-M]);
            }
        }
        System.out.println(dp[3][N]);
    }
}
