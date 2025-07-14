import java.io.*;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.PriorityQueue;
public class Main {
    static int N, K;
    static int[][] board;
    static PriorityQueue<Virus> virusQueue;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        board = new int[N][N];
        virusQueue = new PriorityQueue<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int n = Integer.parseInt(st.nextToken());
                board[i][j] = n;
                if (n != 0) {
                    virusQueue.add(new Virus(n, i, j));
                }
            }
        }

        st = new StringTokenizer(br.readLine());
        int S = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        int Y = Integer.parseInt(st.nextToken());

        int time = 0;
        while (time < S) {
            ArrayList<Virus> arr = new ArrayList<>();
            while (!virusQueue.isEmpty()) {
                Virus cur = virusQueue.poll();
                for (int k = 0; k < 4; k++) {
                    int nr = cur.r + dr[k];
                    int nc = cur.c + dc[k];
                    if (0 <= nr && nr < N && 0 <= nc && nc < N) {
                        if (board[nr][nc] == 0) {
                            board[nr][nc] = cur.num;
                            arr.add(new Virus(cur.num, nr, nc));
                        }
                    }
                }
            }

            for (Virus vir : arr) {
                virusQueue.offer(vir);
            }

            time++;
        }
        System.out.println(board[X-1][Y-1]);
    }
}
class Virus implements Comparable<Virus> {
    int r;
    int c;
    int num;
    public Virus(int num, int r, int c) {
        this.num = num;
        this.r = r;
        this.c = c;

    }

    @Override
    public int compareTo(Virus a) {
        return this.num - a.num;
    }
}