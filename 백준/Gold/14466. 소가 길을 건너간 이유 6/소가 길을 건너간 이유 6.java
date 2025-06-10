import javax.swing.plaf.ViewportUI;
import java.util.*;
import java.io.*;
public class Main {
    static int N, K, R, r1, c1, r2, c2;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int[][] cow;
    static ArrayList<Point>[][] road;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        cow = new int[K][2];
        road = new ArrayList[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                road[i][j] =  new ArrayList<>();
            }
        }

        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            r1 = Integer.parseInt(st.nextToken());
            c1 = Integer.parseInt(st.nextToken());
            r2 = Integer.parseInt(st.nextToken());
            c2 = Integer.parseInt(st.nextToken());

            road[r1-1][c1-1].add(new Point(r2-1, c2-1));
            road[r2-1][c2-1].add(new Point(r1-1, c1-1));
        }

        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            cow[i][0] = r-1;
            cow[i][1] = c-1;
        }

        int answer = 0;

        for (int i = 0; i < K; i++) {
            answer += bfs(cow[i][0], cow[i][1], i);
        }
        System.out.println(answer);


    }

    static int bfs(int r, int c, int idx) {
        Queue<Point> q = new LinkedList<>();
        boolean[][] visited = new boolean[N][N];
        visited[r][c] = true;
        q.add(new Point(r, c));

        while (!q.isEmpty()) {
            Point cur = q.poll();

            for (int k = 0; k < 4; k++) {
                int nr = cur.r + dr[k];
                int nc = cur.c + dc[k];

                if (0 <= nr && nr < N && 0 <= nc && nc < N) {
                    if (!visited[nr][nc]) {
                        boolean possible = true;

                        for (Point next : road[cur.r][cur.c]) {
                            if (nr == next.r && nc == next.c) {
                                possible = false;
                                break;
                            }
                        }
                        if (possible) {
                            q.add(new Point(nr, nc));
                            visited[nr][nc] = true;
                        }
                    }
                }
            }
        }

        int count = 0;
        for (int i = idx+1; i < K; i++) {
            if (!visited[cow[i][0]][cow[i][1]]) {
                count++;
            }
        }
        return count;

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
