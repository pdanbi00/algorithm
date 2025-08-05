import java.io.*;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;
public class Main {
    static int N, M;
    static int[][] board;
    static boolean[][] visited;
    static int[] dr = {0, 1};
    static int[] dc = {1, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        board = new int[M][N];
        visited = new boolean[M][N];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        if (bfs()) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

    }
    static boolean bfs() {
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(0, 0));
        visited[0][0] = true;
        while (!q.isEmpty()) {
            Point cur = q.poll();
            if (cur.r == M-1 && cur.c == N-1) {
                return true;
            }
            for (int k = 0; k < 2; k++) {
                int nr = cur.r + dr[k];
                int nc = cur.c + dc[k];

                if (0 <= nr && nr < M && 0 <= nc && nc < N) {
                    if (board[nr][nc] == 1 && !visited[nr][nc]) {
                        q.add(new Point(nr, nc));
                        visited[nr][nc] = true;
                    }
                }
            }
        }
        return false;
    }
    static class Point{
        int r, c;

        public  Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
}