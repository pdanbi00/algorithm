import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int target = Integer.parseInt(br.readLine());
        int target_r = -1;
        int target_c = -1;

        int[][] board = new int[N][N];
        int cnt = 1;
        int r = N / 2;
        int c = N / 2;
        board[r][c] = 1;
        int num = 2;

        while (cnt <= N / 2) {
            r -= 1;
            if (num == target) {
                target_r = r + 1;
                target_c = c + 1;
            }
            board[r][c] = num;
            num += 1;

            // 오른쪽으로 채우기
            int tmp = 0;
            while (tmp < cnt * 2 - 1) {
                c += 1;
                if (num == target) {
                    target_r = r + 1;
                    target_c = c + 1;
                }
                board[r][c] = num;
                num += 1;
                tmp += 1;
            }

            // 아래쪽으로 채우기
            tmp = 0;
            while (tmp < cnt * 2) {
                r += 1;
                if (num == target) {
                    target_r = r + 1;
                    target_c = c + 1;
                }
                board[r][c] = num;
                num += 1;
                tmp += 1;
            }

            // 왼쪽으로 채우기
            tmp = 0;
            while (tmp < cnt * 2) {
                c -= 1;
                if (num == target) {
                    target_r = r + 1;
                    target_c = c + 1;
                }
                board[r][c] = num;
                num += 1;
                tmp += 1;
            }

            // 위쪽으로 채우기
            tmp = 0;
            while (tmp < cnt * 2) {
                r -= 1;
                if (num == target) {
                    target_r = r + 1;
                    target_c = c + 1;
                }
                board[r][c] = num;
                num += 1;
                tmp += 1;
            }

            cnt += 1;
        }

        if (target == 1) {
            target_r = N / 2 + 1;
            target_c = N / 2 + 1;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sb.append(board[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.print(sb);
        System.out.println(target_r + " " + target_c);
    }
}
