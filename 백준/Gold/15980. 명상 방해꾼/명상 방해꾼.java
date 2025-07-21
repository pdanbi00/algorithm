import java.io.*;
import java.util.StringTokenizer;
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] board = new int[N+1][M];
        int[] sum = new int[M]; // 각 초에서 스님 방해받은 정도

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            char dir = st.nextToken().charAt(0);
            String arr = st.nextToken();
            for (int j = 0; j < M; j++) {
                int value = 0;
                if (arr.charAt(j) == '1') {
                    if (dir == 'L') {
                        value = -1;
                    } else if (dir == 'R') {
                        value = 1;
                    }
                    board[i][j] = value;
                    sum[j] += value;
                }
            }
        }

        int answerSound = 5000000;
        int answerIdx = 0;
        for (int i = 1; i <= N; i++) {
            int total = 0;
            int maxTotal = 0;

            for (int j = 0; j < M; j++) {
                total += sum[j] - board[i][j];
                maxTotal = Math.max(maxTotal, Math.abs(total));
            }

            if (answerSound > maxTotal) {
                answerSound = maxTotal;
                answerIdx = i;
            }
        }
        System.out.println(answerIdx);
        System.out.println(answerSound);

    }
}
