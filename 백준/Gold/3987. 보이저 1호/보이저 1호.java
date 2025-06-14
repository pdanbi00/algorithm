import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static char[][] board;
    static int PR, PC;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    static int[] P = {1, 0, 3, 2};
    static int[] Q = {3, 2, 1, 0};
    static char[] dirs = {'U', 'R', 'D', 'L'};

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
        System.out.println(dirs[idx]);

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
        q.add(new Point(x, y, d));

        while (!q.isEmpty()) {
            cnt++;
            Point cur = q.poll();
            int nr = cur.r + dr[cur.d];
            int nc = cur.c + dc[cur.d];

            if (0 <= nr && nr < N && 0 <= nc && nc < M) {
                if (nr == x && nc == y && cur.d == d) {
                    return Integer.MAX_VALUE;
                }
                if (board[nr][nc] == '.') {
                    q.add(new Point(nr, nc, cur.d));
                } else if (board[nr][nc] == 'C') {
                    return cnt;
                } else if (board[nr][nc] == '/') {
                    q.add(new Point(nr, nc, P[cur.d]));
                } else if (board[nr][nc] == '\\') {
                    q.add(new Point(nr, nc, Q[cur.d]));
                }
            }
        }
        return cnt;
    }
}