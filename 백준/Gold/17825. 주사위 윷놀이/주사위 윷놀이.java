import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;
public class Main {
    static int answer;
    static int[] yut;
    static int[] base = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40};
    static int[] base_10 = {10, 13, 16, 19, 25, 30, 35, 40};
    static int[] base_20 = {20, 22, 24, 25, 30, 35, 40};
    static int[] base_30 = {30, 28, 27, 26, 25, 30, 35, 40};
    static int[] pieces = {0, 0, 0, 0};
    static int[] boardInfo = {0, 0, 0, 0}; // 각 말이 어떤 보드를 다니는지. 0이면 base, 1이면 base_10, 2이면 base_20, 3이면 base_30

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        yut = new int[10];


        for (int i = 0; i < 10; i++) {
            int num = Integer.parseInt(st.nextToken());
            yut[i] = num;
        }

        dfs(0, 0, boardInfo, pieces);
        System.out.println(answer);
    }

    static void dfs(int idx, int score, int[] board, int[] pieces) {
        // 말 4개. 도착 칸에 있지 않은 말을 하나 골라서 주사위에 나온 수 만큼 이동
        // 이동을 마치는 칸에 다른 말이 있으면 안됨.

        // 이동 끝나느 곳이 도착칸이면 괜춘
        // 말 이동 마칠 때마다 칸에 적혀있는 수가 점수에 추가 됨
        if (idx == 10) {
            answer = Math.max(answer, score);
            return;
        }

        for(int i = 0; i < 4; i++) {
            int i_board = board[i];
            int piece_idx = pieces[i];
            if (piece_idx == Integer.MAX_VALUE) { // 이미 도착지에 있는 애들은 패스
                continue;
            }
            int[] b = base;
            if (i_board == 1) {
                b = base_10;
            } else if (i_board == 2) {
                b = base_20;
            } else if (i_board == 3) {
                b = base_30;
            }

            int next = piece_idx + yut[idx];
            if (i_board == 0) {
                if (next >= b.length) {
                    int[] new_board = new int[4];
                    int[] new_pieces = new int[4];
                    for (int k = 0; k < 4; k++) {
                        new_board[k] = board[k];
                        new_pieces[k] = pieces[k];
                    }
                    new_board[i] = i_board;
                    new_pieces[i] = Integer.MAX_VALUE;
                    dfs(idx+1, score, new_board, new_pieces);
                } else {
                    int tmp = base[next];
                    if (tmp == 10) {
                        next = 0;
                        i_board = 1;
                        b = base_10;
                    } else if (tmp == 20) {
                        next = 0;
                        i_board = 2;
                        b = base_20;
                    } else if (tmp == 30) {
                        next = 0;
                        i_board = 3;
                        b = base_30;
                    }
                }

            }
            boolean possible = true;
            if (next >= b.length) {
                int[] new_board = new int[4];
                int[] new_pieces = new int[4];
                for (int k = 0; k < 4; k++) {
                    new_board[k] = board[k];
                    new_pieces[k] = pieces[k];
                }
                new_board[i] = i_board;
                new_pieces[i] = Integer.MAX_VALUE;
                dfs(idx+1, score, new_board, new_pieces);
            } else {
                int tmp = b[next];
                for (int k = 0; k < 4; k++) {
                    if (k == i) {
                        continue;
                    }
                    int[] diff_b = base;
                    if (board[k] == 1) {
                        diff_b = base_10;
                    } else if (board[k] == 2) {
                        diff_b = base_20;
                    } else if (board[k] == 3) {
                        diff_b = base_30;
                    }
                    if (pieces[k] != Integer.MAX_VALUE && diff_b[pieces[k]] == tmp) {
                        if (tmp == 25 || tmp == 35 || tmp == 40) {
                            possible = false;
                            break;
                        } else if (b == diff_b && next == pieces[k]) {
                            possible = false;
                            break;
                        }
                    }
                }
                if (possible) {
                    int[] new_board = new int[4];
                    int[] new_pieces = new int[4];
                    for (int k = 0; k < 4; k++) {
                        new_board[k] = board[k];
                        new_pieces[k] = pieces[k];
                    }
                    new_board[i] = i_board;
                    new_pieces[i] = next;
                    dfs(idx+1, score + b[next], new_board, new_pieces);
                }
            }

        }

    }
    // 3 1 1 5 4 5 3 3 2 5
    // 204
}
