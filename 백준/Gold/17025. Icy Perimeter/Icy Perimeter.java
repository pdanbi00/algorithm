import java.io.*;
import java.util.Queue;
import java.util.LinkedList;
public class Main {
    static int N;
    static char[][] board;
    static boolean[][] visited;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int ans_perimeter, ans_area;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new char[N][N];
        visited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            String arr = br.readLine();
            for (int j = 0; j < N; j++) {
                board[i][j] = arr.charAt(j);
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == '#' && !visited[i][j]) {
                    bfs(i, j);
                }
            }
        }

        System.out.println(ans_area + " " + ans_perimeter);
    }

    static void bfs(int i, int j) {
        Queue<Point> q = new LinkedList<>();
        int perimeter = 0;
        int area = 1;
        q.add(new Point(i, j));
        visited[i][j] = true;

        while (!q.isEmpty()) {
            Point cur = q.poll();
            int tmp = 0;
            for (int k = 0; k < 4; k++) {
                int nr = cur.r + dr[k];
                int nc = cur.c + dc[k];
                if (0 <= nr && nr < N && 0 <= nc && nc < N) {
                    if (board[nr][nc] == '#' && !visited[nr][nc]) {
                        q.add(new Point(nr, nc));
                        visited[nr][nc] = true;
                        area++;
                    } else if (board[nr][nc] == '.') {
                        tmp++;
                    }
                } else {
                    tmp++;
                }
            }
            perimeter += tmp;
        }

        if (area > ans_area) {
            ans_area = area;
            ans_perimeter = perimeter;
        } else if (area == ans_area) {
            if (perimeter < ans_perimeter) {
                ans_perimeter = perimeter;
            }
        }
    }

    static class Point {
        int r;
        int c;

        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
}
