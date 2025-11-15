import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        Queue<int[]> q = new LinkedList<>();
        int[][] visited = new int[R][C];

        int[][] board = new int[R][C];
        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                visited[i][j] = Integer.MAX_VALUE;
                if (i == 0 && board[i][j] == 1) {
                    q.add(new int[] {i, j});
                    visited[i][j] = 0;
                }
            }
        }

        int N = Integer.parseInt(br.readLine());
        int[][] dx = new int[N][2];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 2; j++) {
                dx[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int answer = Integer.MAX_VALUE;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            if (cur[0] == R-1) {
                answer = visited[cur[0]][cur[1]];
                break;
            }

            for (int k = 0; k < N; k++) {
                int nr = cur[0] + dx[k][0];
                int nc = cur[1] + dx[k][1];

                if (0 <= nr && nr < R && 0 <= nc && nc < C) {
                    if (board[nr][nc] == 1 && visited[nr][nc] == Integer.MAX_VALUE) {
                        q.add(new int[] {nr, nc});
                        visited[nr][nc] = visited[cur[0]][cur[1]] + 1;
                    }
                }
            }
        }

        if (answer == Integer.MAX_VALUE) {
            System.out.println(-1);
        } else {
            System.out.println(answer);
        }
    }
}
