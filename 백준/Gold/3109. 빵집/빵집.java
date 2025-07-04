import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
public class Main {
    static int R, C;
    static char[][] board;
    static int[] dr = {-1, 0, 1};
    static int[] dc = {1, 1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        board = new char[R][C];
        for (int i = 0; i < R; i++) {
            String arr = br.readLine();
            for (int j = 0; j < C; j++) {
                board[i][j] = arr.charAt(j);
            }
        }
        int answer = 0;
        for (int i = 0; i < R; i++) {
            if (board[i][0] == '.') {
                if (dfs(i, 0)) {
                    answer++;
                }
            }
        }
        System.out.println(answer);
    }
    static boolean dfs(int r, int c) {
        if (c == C-1) {
            return true;
        }

        for (int k = 0; k < 3; k++) {
            int nr = r + dr[k];
            int nc = c + dc[k];
            if (0 <= nr && nr < R && 0 <= nc && nc < C) {
                if (board[nr][nc] == '.') {
                    board[nr][nc] = 'o';
                    if (dfs(nr, nc)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
