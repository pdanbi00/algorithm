import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        int[][] board = new int[M][M];
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < M; j++) {
                board[i][j] = 1;
            }
        }
        int[] glow = new int[2*M-1];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int[] cnt = new int[3];
            for (int k = 0; k < 3; k++) {
                cnt[k] = Integer.parseInt(st.nextToken());
            }

            for (int j = cnt[0]; j < cnt[0] + cnt[1]; j++) {
                glow[j] += 1;
            }

            for (int j = cnt[0] + cnt[1]; j < 2*M-1; j++) {
                glow[j] += 2;
            }
        }

        int idx = 0;
        // 제일 왼쪽 열 채우기
        for (int i = M-1; i > 0; i--) {
            board[i][0] += glow[idx];
            idx++;
        }
        // 제일 위쪽 행 채우기
        for (int j = 0; j < M; j++) {
            board[0][j] += glow[idx];
            idx++;
        }

        // 나머지 칸 채우기
        // 항상 자기자신의 바로 위 칸이 최대 성장임
        for (int i = 1 ; i < M; i++) {
            for (int j = 1; j < M; j++) {
                board[i][j] = board[i-1][j];
            }
        }

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < M; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }
}
