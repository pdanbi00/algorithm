import java.util.*;
import java.io.*;
public class Main {
    static int N;
    static int[][] board;
    static int answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        answer = Integer.MAX_VALUE;

//        func(3, 2, 1, 1);

        for (int i = 0 ; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int d1 = 1; d1 < N; d1++) {
                    for (int d2 = 1; d2 < N; d2++) {
                        if ((i + d1 + d2 < N) && (j - d1 >= 0) && (j + d2 < N)) {
                            answer = Integer.min(func(i, j, d1, d2), answer);
                        }
                    }
                }
            }
        }
        System.out.println(answer);
    }

    public static int func(int r, int c, int d1, int d2) {
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        int[][] visited = new int[N][N];
        int[] tmp = new int[5];

        // 1번 경계선 긋기
        int dr = 0;
        int dc = 0;
        while (dr <= d1 && dc >= -d1) {
            visited[r+dr][c+dc] = 5;
            dr++;
            dc--;
        }

        // 2번 경계선 긋기
        dr = 0;
        dc = 0;
        while (dr <= d2 && dc <= d2) {
            visited[r+dr][c+dc] = 5;
            dr++;
            dc++;
        }

        // 3번 경계선 긋기
        dr = 0;
        dc = 0;
        while (dr <= d2 && dc <= d2) {
            visited[r+d1+dr][c-d1+dc] = 5;
            dr++;
            dc++;
        }

        // 4번 경계선 긋기
        dr = 0;
        dc = 0;
        while (dr <= d1 && dc >= -d1) {
            visited[r+d2+dr][c+d2+dc] = 5;
            dr++;
            dc--;
        }

        // 1번 선거구 계산하기
        for (int i = 0; i < r + d1; i++) {
            for (int j = 0; j <= c; j++) {
                if (visited[i][j] == 5) {
                    break;
                }
                visited[i][j] = 1;
                tmp[0] += board[i][j];
            }
        }

        // 2번 선거구 계산하기
        for (int i = 0; i <= r + d2; i++) {
            for (int j = N-1; j > c; j--) {
                if (visited[i][j] == 5) {
                    break;
                }
                visited[i][j] = 2;
                tmp[1] += board[i][j];
            }
        }

        // 3번 선거구 계산하기
        for (int i = r + d1; i < N; i++) {
            for (int j = 0; j < c - d1 + d2; j++) {
                if (visited[i][j] == 5) {
                    break;
                }
                visited[i][j] = 3;
                tmp[2] += board[i][j];
            }
        }

        // 4번 선거구 계산하기
        for (int i = r + d2 + 1; i < N; i++) {
            for (int j = N-1; j >= c - d1 + d2; j--) {
                if (visited[i][j] == 5) {
                    break;
                }
                visited[i][j] = 4;
                tmp[3] += board[i][j];
            }
        }

        // 5번 선거구 계산하기
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (visited[i][j] == 0 || visited[i][j] == 5) {
                    tmp[4] += board[i][j];
                }

            }
        }
        for (int i = 0; i < 5; i++) {
            if (tmp[i] > max) {
                max = tmp[i];
            }
            if (tmp[i] < min) {
                min = tmp[i];
            }
        }

        return max - min;
    }
}
