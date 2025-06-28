import java.util.*;
import java.io.*;
public class Main {
    static char[][] board;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        board = new char[N][N];

        star(0, 0, N, false);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sb.append(board[i][j]);
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }
    // 시작 행, 열, 크기, 공백여부
    static void star(int r, int c, int n, boolean blank) {
        // 공백일 경우
        if (blank) {
            for (int i = r; i < r + n; i++) {
                for (int j = c; j < c + n; j++) {
                    board[i][j] = ' ';
                }
            }
            return;
        }

        // 더이상 쪼갤 수 없을 경우
        if (n <= 1) {
            board[r][c] = '*';
            return;
        }

        int blockSize = n/3; // 한 블록의 사이즈 구하기
        int starCnt = 0; // 별 공백 기준 체크 하기
        for (int i = r; i < r + n; i += blockSize) {
            for (int j = c; j < c+n; j += blockSize) {
                starCnt++;
                // 9개의 구역으로 나눴을 때 5번째 구역이 무조건 공백
                if (starCnt == 5) {
                    star(i, j, blockSize, true);
                } else {
                    star(i, j, blockSize, false);
                }
            }
        }
    }

}
