import java.nio.Buffer;
import java.util.*;
import java.io.*;
public class Main {
    static int[][] board = new int[5][5];
    static int answer = 0;
    static int count = 0;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        // 빙고판 입력받기
        for (int i = 0; i < 5; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        // 숫자 하나씩 부르기
        for (int i = 0; i < 5; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                answer++;
                bingo(Integer.parseInt(st.nextToken()));
                count = 0;
                rCheck();
                cCheck();
                xyCheck();
                yxCheck();
                if (count >= 3) {
                    System.out.println(answer);
                    return;
                }
            }
        }

    }
    // 부른 숫자 처리(-1)
    public static void bingo(int n) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (board[i][j] == n) {
                    board[i][j] = -1;
                }
            }
        }
    }

    // 빙고 확인(행)
    public static void rCheck() {
        for (int i = 0; i < 5; i++) {
            int c = 0;
            for (int j = 0; j < 5; j++) {
                if (board[i][j] == -1) {
                    c += 1;
                }
            }
            if (c == 5) {
                count++;
            }
        }

    }

    // 빙고 확인(열)
    public static void cCheck() {
        for (int j = 0; j < 5; j++) {
            int c = 0;
            for (int i = 0; i < 5; i++) {
                if (board[i][j] == -1) {
                    c += 1;
                }
            }
            if (c == 5) {
                count++;
            }
        }

    }

    // 빙고 확인(오른쪽 아래)
    public static void xyCheck() {
        int c = 0;
        for (int i = 0; i < 5; i++) {
            if (board[i][i] == -1) {
                c += 1;
            }
        }
        if (c == 5) {
            count++;
        }

    }

    // 빙고 확인(오른쪽 위)
    public static void yxCheck() {
        int c = 0;
        for (int i = 0; i < 5; i++) {
            if (board[i][4-i] == -1) {
                c += 1;
            }
        }
        if (c == 5) {
            count++;
        }

    }
}
