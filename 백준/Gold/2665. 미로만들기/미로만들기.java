import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.ArrayDeque;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] board = new int[N][N];
        int[][] visited = new int[N][N];

        for (int i = 0; i < N; i++) {
            String arr = br.readLine();
            for (int j = 0; j < N; j++) {
                board[i][j] = arr.charAt(j) - '0';
                visited[i][j] = Integer.MAX_VALUE;
            }
        }

        Deque<int[]> q = new ArrayDeque<>();
        q.offer(new int[] {0, 0, 0});
        visited[0][0] = 0;

        int[] dr = new int[] {-1, 1, 0, 0};
        int[] dc = new int[] {0, 0, -1, 1};

        int nr, nc;
        int[] cur;

        while (!q.isEmpty()) {
            cur = q.poll();
            int dist = cur[2];

            if (visited[cur[0]][cur[1]] < dist) {
                continue;
            }

            for (int k = 0; k < 4; k++) {
                nr = cur[0] + dr[k];
                nc = cur[1] + dc[k];

                if (0 <= nr && nr < N && 0 <= nc && nc < N) {
                    if (board[nr][nc] == 1) {
                        if (visited[nr][nc] > dist) {
                            visited[nr][nc] = dist;
                            q.addFirst(new int[] {nr, nc, visited[nr][nc]});
                        }
                    } else if (board[nr][nc] == 0) {
                        if (visited[nr][nc] > dist + 1) {
                            visited[nr][nc] = dist + 1;
                            q.addLast(new int[] {nr, nc, visited[nr][nc]});
                        }
                    }
                }
            }
        }
        System.out.print(visited[N-1][N-1]);
    }
}
