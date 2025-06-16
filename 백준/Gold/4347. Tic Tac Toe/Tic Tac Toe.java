import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static char[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < N; tc++) {
            board = new char[3][3];
            int o_cnt = 0;
            int x_cnt = 0;
            for (int i = 0; i < 3; i++) {
                String arr = br.readLine();
                for (int j = 0; j < 3; j++) {
                    board[i][j] = arr.charAt(j);
                    if (board[i][j] == 'O') {
                        o_cnt++;
                    } else if (board[i][j] == 'X') {
                        x_cnt++;
                    }
                }
            }
            if (tc < N-1) {
                String tmp = br.readLine();
            }
            // O가 이겼는지 확인하기
            boolean o_win = false;
            for (int i = 0; i < 3; i++) {
                if (board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][2] == 'O') {
                    o_win = true;
                }
                if (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[2][i] == 'O') {
                    o_win = true;
                }
            }
            if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[2][2] == 'O') {
                o_win = true;
            }
            if (board[2][0] == board[1][1] && board[1][1] == board[0][2] && board[0][2] == 'O') {
                o_win = true;
            }

            // X가 이겼는지 확인하기
            boolean x_win = false;
            for (int i = 0; i < 3; i++) {
                if (board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][2] == 'X') {
                    x_win = true;
                }
                if (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[2][i] == 'X') {
                    x_win = true;
                }
            }
            if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[2][2] == 'X') {
                x_win = true;
            }
            if (board[2][0] == board[1][1] && board[1][1] == board[0][2] && board[0][2] == 'X') {
                x_win = true;
            }

            boolean answer = false;
            if (x_cnt == o_cnt + 1) {
                if ((!x_win && !o_win) || (x_win && !o_win)) {
                    answer = true;
                }
            } else if (x_cnt == o_cnt) {
                if ((!x_win && !o_win) || (!x_win && o_win)) {
                    answer = true;
                }
            }

            if (answer) {
                System.out.println("yes");
            } else {
                System.out.println("no");
            }


        }
    }
}
