import java.io.*;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] board = new int[101][101];
        for (int p = 0; p < 4; p++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int c1 = Integer.parseInt(st.nextToken());
            int r1 = Integer.parseInt(st.nextToken());
            int c2 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());
            for (int i = r1; i < r2; i++) {
                for (int j = c1; j < c2; j++) {
                    board[i][j]++;
                }
            }
        }
        int answer = 0;
        for (int i = 0; i < 101; i++) {
            for (int j = 0; j < 101; j++) {
                if (board[i][j] != 0) {
                    answer++;
                }
            }
        }
        System.out.println(answer);
    }
}
