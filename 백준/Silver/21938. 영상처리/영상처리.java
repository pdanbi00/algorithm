import java.util.*;
import java.io.*;
public class Main {
    static int N, M, T;
    static int[][] board;
    static boolean[][] visited;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int R = Integer.parseInt(st.nextToken());
                int G = Integer.parseInt(st.nextToken());
                int B = Integer.parseInt(st.nextToken());
                int tmp = (R + G + B) / 3;
                board[i][j] = tmp;
            }
        }
        st = new StringTokenizer(br.readLine());
        T = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N;i ++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] >= T) {
                    board[i][j] = 1;
                } else {
                    board[i][j] = 0;
                }
            }
        }

        int answer = 0;
        visited = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == 1 && !visited[i][j]) {
                    bfs(i, j);
                    answer++;
                }
            }
        }
        System.out.println(answer);


    }

    static void bfs(int x, int y) {
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(x, y));
        visited[x][y] = true;
        while (!q.isEmpty()) {
            Point cur = q.poll();
            for (int k = 0; k < 4; k++) {
                int nr = cur.r + dr[k];
                int nc = cur.c + dc[k];
                if (0 <= nr && nr < N && 0 <= nc && nc < M) {
                    if (board[nr][nc] == 1 && !visited[nr][nc]) {
                        q.add(new Point(nr, nc));
                        visited[nr][nc] = true;
                    }
                }

            }

        }
    }

    static class Point {
        int r;
        int c;

        Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
}
