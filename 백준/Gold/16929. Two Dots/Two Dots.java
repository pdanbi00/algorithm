import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static char[][] board;
    static boolean[][] visited;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void dfs(int s_r, int s_c, int r, int c, int cnt) {
        for (int k = 0; k < 4; k++) {
            int nr = r + dr[k];
            int nc = c + dc[k];

            if (nr < 0 || nr >= n || nc < 0 || nc >= m) {
                continue;
            } else if (!(visited[nr][nc]) && board[nr][nc] == board[r][c]) {
                visited[nr][nc] = true;
                dfs(s_r, s_c, nr, nc, cnt+1);
                visited[nr][nc] = false;
            } else if (cnt >= 4 && nr == s_r && nc == s_c) {
                System.out.println("Yes");
                System.exit(0);
                return;
            }
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        board = new char[n][m];
        visited = new boolean[n][m];

        // 배열 입력받기
        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            for (int j = 0; j < m; j++) {
                board[i][j] = str.charAt(j);
            }
        }

        // dfs 실행
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                visited[i][j] = true;
                dfs(i, j, i, j, 1);
                visited[i][j] = false;
            }
        }

        System.out.println("No");
    }
}
