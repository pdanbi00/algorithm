import java.util.*;
import java.io.*;

public class Main {
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int[][] board;
    static int s_r;
    static int s_c;
    static int N;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        int fish_size = 2; // 현재 상어 크기
        int eat_cnt = 0; // 상어가 지금까지 먹은 물고기 수
        board = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());

                if (board[i][j] == 9) {
                    s_r = i; // 상어 위치 r
                    s_c = j; // 상어 위치 c
                    board[i][j] = 0; // 상어 있던 위치 0으로 초기화
                }
            }
        }
        int time = 0;

        while (true) {
            // 현재 위치에서 전체 bfs 돌면서 먹을 수 있는 물고기 담기
            List<int[]> fishes = bfs(s_r, s_c, fish_size);

            if (fishes.isEmpty()) {
                break;
            }

            fishes.sort((a, b) -> {
                if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
                if (a[1] != b[1]) return Integer.compare(a[1], b[1]);
                return Integer.compare(a[2], b[2]);
            });

            time += fishes.get(0)[0];
            eat_cnt += 1;

            if (eat_cnt == fish_size) {
                fish_size ++;
                eat_cnt = 0;
            }

            s_r = fishes.get(0)[1];
            s_c = fishes.get(0)[2];
            board[s_r][s_c] = 0;
        }
        System.out.println(time);

    }
    static List<int[] > bfs(int s_r, int s_c, int f_size) {
        List<int[]> fishes = new ArrayList<>();
        int[][] visited = new int[N][N];
        for (int[] row : visited) Arrays.fill(row, -1);

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {s_r, s_c});
        visited[s_r][s_c] = 0;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int r = current[0], c = current[1];

            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];

                if (nr >= 0 && nr < N && nc >= 0 && nc < N && visited[nr][nc] == -1 && board[nr][nc] <= f_size) {
                    visited[nr][nc] = visited[r][c] + 1;
                    queue.add(new int[] {nr, nc});

                    if (board[nr][nc] > 0 && board[nr][nc] < f_size) {
                        fishes.add(new int[] {visited[nr][nc], nr, nc});
                    }
                }
            }
        }
        return fishes;
    }
}
