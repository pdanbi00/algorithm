import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static char[][] board;
    static int PR, PC;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new char[N][M];
        for (int i = 0; i < N; i++) {
            String arr = br.readLine();
            for (int j = 0; j < M; j++) {
                board[i][j] = arr.charAt(j);
            }
        }
        st = new StringTokenizer(br.readLine());
        PR = Integer.parseInt((st.nextToken()));
        PC = Integer.parseInt((st.nextToken()));

        int[] answer = new int[4];

        for (int i = 0; i < 4; i++) {
            answer[i] = func(PR - 1, PC - 1, i);
        }
        int max = answer[0];
        int idx = 0;
        for (int i = 1; i < 4; i++) {
            if (answer[i] > max) {
                max = answer[i];
                idx = i;
            }
        }
        if (idx == 0) {
            System.out.println('U');
        } else if (idx == 1) {
            System.out.println('R');
        } else if (idx == 2) {
            System.out.println('D');
        } else {
            System.out.println('L');
        }

        if (max == Integer.MAX_VALUE) {
            System.out.println("Voyager");
        } else {
            System.out.println(max);
        }
    }

    static class Point {
        int r;
        int c;
        int d;

        Point(int r, int c, int d) {
            this.r = r;
            this.c = c;
            this.d = d;
        }
    }

    static int func(int x, int y, int d) {
        int cnt = 0;
        Queue<Point> q = new LinkedList<>();
        boolean[][][] visited = new boolean[N][M][4];
        q.add(new Point(x, y, d));
        visited[x][y][d] = true;

        while (!q.isEmpty()) {
            cnt++;
            Point cur = q.poll();
            int nr = cur.r + dr[cur.d];
            int nc = cur.c + dc[cur.d];

            if (0 <= nr && nr < N && 0 <= nc && nc < M) {
                if (!visited[nr][nc][cur.d]) {
                    if (board[nr][nc] == '.') {
                        q.add(new Point(nr, nc, cur.d));
                        visited[nr][nc][cur.d] = true;
                    } else if (board[nr][nc] == 'C') {
                        return cnt;
                    } else if (board[nr][nc] == '/') {
                        visited[nr][nc][cur.d] = true;
                        if (cur.d == 0) {
                            q.add(new Point(nr, nc, 1));
                        } else if (cur.d == 1) {
                            q.add(new Point(nr, nc, 0));
                        } else if (cur.d == 2) {
                            q.add(new Point(nr, nc, 3));
                        } else if (cur.d == 3) {
                            q.add(new Point(nr, nc, 2));
                        }
                    } else if (board[nr][nc] == '\\') {
                        visited[nr][nc][cur.d] = true;
                        if (cur.d == 0) {
                            q.add(new Point(nr, nc, 3));
                        } else if (cur.d == 1) {
                            q.add(new Point(nr, nc, 2));
                        } else if (cur.d == 2) {
                            q.add(new Point(nr, nc, 1));
                        } else if (cur.d == 3) {
                            q.add(new Point(nr, nc, 0));
                        }
                    }
                } else {
                    return Integer.MAX_VALUE;
                }
            }
        }
        return cnt;
    }
}