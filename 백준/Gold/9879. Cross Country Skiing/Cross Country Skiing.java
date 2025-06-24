// 이분탐색 + bfs
import java.util.*;
import java.io.*;
public class Main {
    static int M, N;
    static int[][] board;
    static ArrayList<Integer> points;
    static HashSet<Integer> set;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        board = new int[M][N];

        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                min = Math.min(min, board[i][j]);
                max = Math.max(max, board[i][j]);
            }
        }

        points = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int tmp = Integer.parseInt(st.nextToken());
                if (tmp == 1) {
                    points.add(i * N + j);
                }
            }
        }

        int left = 0;
        int right = max - min;
        int ans = -1;

        while (left <= right) {
            int mid = (left + right) / 2;
            set = new HashSet<>();
            int start = points.get(0);
            boolean possible = true;

            bfs(start/N, start%N, mid);

            for (int i = 0; i < points.size(); i++) {
                int p = points.get(i);

                if (!set.contains(p)) {
                    possible = false;
                    break;
                }
            }

            if (!possible) {
                left = mid + 1;
            } else {
                ans = mid;
                right = mid - 1;

            }
        }

        System.out.println(ans);


    }

    public static void bfs(int r, int c, int d) { // 정해진 D를 이용해서 갈 수 있는 모든 포인트 찾기
        Queue<Point> q = new LinkedList<>();
        boolean[][] visited = new boolean[M][N];
        set.add(r * N + c);
        q.add(new Point(r, c));
        visited[r][c] = true;
        while (!q.isEmpty()) {
            Point cur = q.poll();

            for (int k = 0; k < 4; k++) {
                int nr = cur.r + dr[k];
                int nc = cur.c + dc[k];
                if (0 <= nr && nr < M && 0 <= nc && nc < N) {
                    if (Math.abs(board[cur.r][cur.c] - board[nr][nc]) <= d && !visited[nr][nc]) {
                        q.add(new Point(nr, nc));
                        set.add(nr * N + nc);
                        visited[nr][nc] = true;
                    }
                }
            }
        }


    }

    public static class Point {
        int r;
        int c;
        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }


    }
}
