import java.io.*;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;
        for (int tc = 1; tc <= T; tc++) {
            int[][] board = new int[9][9];
            for (int i = 0; i < 9; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 9; j++) {
                    board[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            if (tc < T) {
                String tmp = br.readLine();
            }

            boolean result = check(board);
            if (result) {
                System.out.printf("Case " + tc + ": CORRECT\n");
            } else {
                System.out.printf("Case " + tc + ": INCORRECT\n");
            }
        }
    }

    static boolean check(int[][] arr) {
        for (int i = 0; i < 9; i++) {
            boolean[] visitedSero = new boolean[10];
            boolean[] visitedGaro = new boolean[10];
            for (int j = 0; j < 9; j++) {
                if (visitedSero[arr[i][j]]) {
                    return false;
                } else {
                    visitedSero[arr[i][j]] = true;
                }

                if (visitedGaro[arr[j][i]]) {
                    return false;
                } else {
                    visitedGaro[arr[j][i]] = true;
                }

                boolean[] visitedThree = new boolean[10];
                if (i % 3 == 0 && j % 3 == 0) {
                    for (int k = 0; k < 3; k++) {
                        for (int p = 0; p < 3; p++) {
                            if (visitedThree[arr[i+k][j+p]]) {
                                return false;
                            } else {
                                visitedThree[arr[i+k][j+p]] = true;
                            }
                        }
                    }
                }
            }
        }
        return true;
    }
}