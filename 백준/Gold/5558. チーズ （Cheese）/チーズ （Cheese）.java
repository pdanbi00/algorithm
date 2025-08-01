import java.io.*;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Queue;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Collections;
public class Main {
    static int H, W, N;
    static char[][] board;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    static int answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        H = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
;
        board = new char[H][W];
        ArrayList<Cheese> cheeses = new ArrayList<>();

        for (int i = 0; i < H; i++) {
            String arr = br.readLine();
            for (int j = 0; j < W; j++) {
                board[i][j] = arr.charAt(j);
                if (board[i][j] == 'S') {
                    cheeses.add(new Cheese(0, i, j));
                } else if (Character.isDigit(board[i][j])) {
                    cheeses.add(new Cheese(board[i][j] - '0', i, j));
                }
            }
        }
        Collections.sort(cheeses);
        answer = 0;
        for (int i = 0; i < N; i++) {
            bfs(cheeses.get(i).r, cheeses.get(i).c, cheeses.get(i+1).r, cheeses.get(i+1).c);
        }
        System.out.println(answer);
    }

    static void bfs(int s_r, int s_c, int e_r, int e_c) {
        Queue<int[]> q = new LinkedList<>();
        int[][] visited = new int[H][W];
        q.add(new int[] {s_r, s_c});
        for (int i = 0; i < H; i++) {
            Arrays.fill(visited[i], -1);
        }
        visited[s_r][s_c] = 0;
        while (!q.isEmpty()) {
            int[] cur = q.poll();

            if (cur[0] == e_r && cur[1] == e_c) {
                answer += visited[cur[0]][cur[1]];
                break;
            }

            for (int k = 0; k < 4; k++) {
                int nr = cur[0] + dr[k];
                int nc = cur[1] + dc[k];

                if (0 <= nr && nr < H && 0 <= nc && nc < W) {
                    if (visited[nr][nc] == -1 && board[nr][nc] != 'X') {
                        q.add(new int[] {nr, nc});
                        visited[nr][nc] = visited[cur[0]][cur[1]] + 1;
                    }
                }
            }
        }
    }


}
class Cheese implements Comparable<Cheese>{
    int idx, r, c;

    public Cheese(int idx, int r, int c) {
        this.idx = idx;
        this.r = r;
        this.c = c;
    }

    @Override
    public int compareTo(Cheese other) {
        return Integer.compare(this.idx, other.idx);
    }
}