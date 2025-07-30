import java.io.*;
import java.util.StringTokenizer;
import java.util.Arrays;
public class Main {
    static int N;
    static int[][] map;
    static int[][] dp;
    static StringTokenizer st = null;
    static int INF = 17000000;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        // dp[i][j] : 현재 있는 도시가 i이고 이미 방문한 도시들의 집합이 j일때 방문하지 않은 나머지 도시들을 모두 방문한 뒤 출발도시로로 돌아올때 드는 최소 비용
        dp = new int[N][1<<N];
        for (int i = 0; i < N; i++) {
            Arrays.fill(dp[i], -1);
        }
        System.out.println(tsp(0, 1)); // 0번 도시부터 탐색, bitState : 0001
    }

    static int tsp(int x, int bitState) {
        // 모든 도시 방문 완료
        if (bitState == (1 << N) - 1) {
            if (map[x][0] == 0) { // 경로 없으면 탐색 무효화
                return INF;
            } else {
                return map[x][0];
            }
        }

        if (dp[x][bitState] != -1) { // 이미 방문한 도시
            return dp[x][bitState];
        }

        // x 도시 방문 표시
        dp[x][bitState] = INF;

        for (int i = 0; i < N; i++) {
            // next : 다음으로 방문할 i 도시
            int next = bitState | (1 << i);

            // 경로가 있고, 방문 하지 않은 경우
            if (map[x][i] != 0 && (bitState & (1 << i)) == 0 ) {
                dp[x][bitState] = Math.min(dp[x][bitState], tsp(i, next) + map[x][i]);
            }
        }

        return dp[x][bitState];
    }
}
