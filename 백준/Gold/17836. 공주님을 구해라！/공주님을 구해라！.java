import java.io.*;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Arrays;
public class Main {
    static int N, M, T, g_r, g_c;
    static int[][] board;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());

        board = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 2) {
                    g_r = i; // 그람 위치 행
                    g_c = j; // 그람 위치 열
                }
            }
        }

        int answer = bfs(new Point(0, 0), new Point(N-1, M-1), false);
        int sword_cnt = bfs(new Point(0, 0), new Point(g_r, g_c), false);
        if (sword_cnt != -1) {
            sword_cnt += bfs(new Point(g_r, g_c), new Point(N-1, M-1), true);
            if (answer != -1) {
                int tmp = Math.min(answer, sword_cnt);
                if (tmp <= T) {
                    System.out.println(tmp);
                } else {
                    System.out.println("Fail");
                }
            } else {
                if (sword_cnt <= T) {
                    System.out.println(sword_cnt);
                } else {
                    System.out.println("Fail");
                }
            }
        } else {
            if (answer == -1) {
                System.out.println("Fail");
            } else {
                if (answer <= T) {
                    System.out.println(answer);
                } else {
                    System.out.println("Fail");
                }
            }
        }

    }
    static int bfs(Point start, Point target, boolean sword) {
        Queue<Point> q = new LinkedList<>();
        int[][] visited = new int[N][M];
        for (int i = 0; i < N; i++) {
            Arrays.fill(visited[i], -1);
        }

        q.add(start);
        visited[start.r][start.c] = 0;
        while (!q.isEmpty()) {
            Point cur = q.poll();
            if (cur.r == target.r && cur.c == target.c) {
                return visited[cur.r][cur.c];
            }

            for (int k = 0; k < 4; k++) {
                int nr = cur.r + dr[k];
                int nc = cur.c + dc[k];
                if (0 <= nr && nr < N && 0 <= nc && nc < M) {
                    if (sword) { // 칼 가지고 있으면 벽 있어도 통과 가능
                        if (visited[nr][nc] == -1) {
                            q.add(new Point(nr, nc));
                            visited[nr][nc] = visited[cur.r][cur.c] + 1;
                        }

                    } else {
                        if ((board[nr][nc] == 0 || board[nr][nc] == 2)  && visited[nr][nc] == -1) {
                            q.add(new Point(nr, nc));
                            visited[nr][nc] = visited[cur.r][cur.c] + 1;
                        }
                    }
                }
            }
        }
        return -1;
    }

    static class Point {
        int r, c;

        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
}

