import java.io.*;
import java.util.LinkedList;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Queue;
public class Main {
    static int N, K;
    static int[][] board;
    static ArrayList<ArrayList> virusArr;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        board = new int[N][N];
        virusArr = new ArrayList<>();
        for (int i = 0; i <= K; i++) {
            ArrayList<Virus> arr = new ArrayList<>();
            virusArr.add(arr);
        }
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int n = Integer.parseInt(st.nextToken());
                board[i][j] = n;
                if (n != 0) {
                    virusArr.get(n).add(new Virus(i, j, n));
                }
            }
        }

        st = new StringTokenizer(br.readLine());
        int S = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        int Y = Integer.parseInt(st.nextToken());

        int time = 0;
        while (time < S) {
            Queue<Virus> q = new LinkedList<>();
            for (int i = 1; i <= K; i++) {
                ArrayList<Virus> vArr = virusArr.get(i);
                for (int j = 0; j < vArr.size(); j++) {
                    q.offer(vArr.get(j));
                }
                virusArr.get(i).clear();
            }
            while (!q.isEmpty()) {
                Virus cur = q.poll();
                for (int k = 0; k < 4; k++) {
                    int nr = cur.r + dr[k];
                    int nc = cur.c + dc[k];
                    if (0 <= nr && nr < N && 0 <= nc && nc < N) {
                        if (board[nr][nc] == 0) {
                            board[nr][nc] = cur.num;
                            virusArr.get(cur.num).add(new Virus(nr, nc, cur.num));
                        }
                    }
                }
            }
            time++;
        }
        System.out.println(board[X-1][Y-1]);
    }
}
class Virus {
    int r;
    int c;
    int num;
    public Virus(int r, int c, int num) {
        this.r = r;
        this.c = c;
        this.num = num;
    }
}
