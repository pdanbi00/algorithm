import java.io.*;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int[] dr = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dc = {-1, 0, 1, -1, 1, -1, 0, 1};
        while (true) {
            st = new StringTokenizer(br.readLine());
            int R = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());
            if (R == 0 && C == 0) {
                break;
            }

            char[][] board = new char[R][C];
            for (int i = 0; i < R; i++) {
                String arr = br.readLine();
                for (int j = 0; j < C; j++) {
                    board[i][j] = arr.charAt(j);
                }
            }

            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    if (board[i][j] == '.') {
                        int cnt = 0;
                        for (int k = 0; k < 8; k++) {
                            int nr = i + dr[k];
                            int nc = j + dc[k];
                            if (0 <= nr && nr < R && 0 <= nc && nc < C) {
                                if (board[nr][nc] == '*') {
                                    cnt += 1;
                                }
                            }
                        }
                        sb.append(cnt);
                    } else {
                        sb.append('*');
                    }

                }
                sb.append("\n");
            }
        }
        System.out.println(sb);
    }
}
