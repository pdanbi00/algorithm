import java.io.*;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        int N = Integer.parseInt(br.readLine());
        int r = 0;
        int c = 0;
        int w = 0;
        int h = 0;
        int[][] board = new int[1001][1001];

        for (int n = 1; n <= N; n++) {
            st = new StringTokenizer(br.readLine());
            c = Integer.parseInt(st.nextToken());
            r = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());

            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    board[100-r-i][c+j] = n;
                }
            }
        }

        int[] answer = new int[N+1];

        for (int i = 0; i < 1001; i++) {
            for (int j = 0; j < 1001; j++) {
                for (int k = 1; k <= N; k++) {
                    if (board[i][j] == k) {
                        answer[k]++;
                    }
                }
            }
        }

        for (int i = 1; i <= N; i++) {
            System.out.println(answer[i]);
        }
    }
}
