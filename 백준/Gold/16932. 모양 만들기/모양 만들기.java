import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    static int[][] visited;
    static int[][] board;
    static int N, M, idx;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static Map<Integer, Integer> bfsInfo;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        visited = new int[N][M];
        board = new int[N][M];
        List<Dot> zero = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int num = Integer.parseInt(st.nextToken());
                board[i][j] = num;
                if (num == 0) {
                    zero.add(new Dot(i, j));
                }
            }
        }
        idx = 1;
        bfsInfo = new HashMap<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == 1 && visited[i][j] == 0) {
                    bfs(i, j);
                }
            }
        }
        int ans = 0;
        for (Dot cur : zero) {
            int total = 1;
            List<Integer> used = new ArrayList<>();
            for (int k = 0; k < 4; k++) {
                int nr = cur.r + dr[k];
                int nc = cur.c + dc[k];
                if (0 <= nr && nr < N && 0 <= nc && nc < M) {
                    if (visited[nr][nc] != 0 && !used.contains(visited[nr][nc])) {
                        used.add(visited[nr][nc]);
                        total += bfsInfo.get(visited[nr][nc]);
                    }
                }
            }
            ans = Math.max(ans, total);
        }
        System.out.println(ans);
    }

    static void bfs(int x, int y) {
        Queue<Dot> q = new LinkedList<>();
        q.add(new Dot(x, y));
        visited[x][y] = idx;
        int cnt = 0;
        while (!q.isEmpty()) {
            Dot cur = q.poll();
            cnt++;
            for (int k = 0; k < 4; k++) {
                int nr = cur.r + dr[k];
                int nc = cur.c + dc[k];

                if (0 <= nr && nr < N && 0 <= nc && nc < M) {
                    if (board[nr][nc] == 1 && visited[nr][nc] == 0) {
                        q.add(new Dot(nr, nc));
                        visited[nr][nc] = idx;
                    }
                }
            }
        }
        bfsInfo.put(idx, cnt);
        idx++;
    }

}

class Dot {
    int r, c;

    public Dot(int r, int c) {
        this.r = r;
        this.c = c;
    }
}