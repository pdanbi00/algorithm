import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        boolean[] v = new boolean[n];
        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        boolean possible = true;
        for (int i = 0; i < n; i++) {
            if (v[i]) continue;
            v[i] = true;
            List<Integer> tmp = new ArrayList<>();
            tmp.add(i);

            for (int j = 0; j < n; j++) {
                if (i == j || board[i][j] == 1) continue;
                if (v[j]) {
                    possible = false;
                    break;
                }
                v[j] = true;
                tmp.add(j);
            }

            if (tmp.size() < 2) {
                possible = false;
                break;
            }

            for (int cur1 : tmp) {
                for (int cur2 : tmp) {
                    if (board[cur1][cur2] == 1) {
                        possible = false;
                        break;
                    }
                }
                if (!possible) {
                    break;
                }
            }
            if (possible) {
                cnt++;
                for (int cur : tmp) {
                    sb.append(cur+1).append(' ');
                }
                sb.append('\n');
            }
        }

        if (possible) {
            System.out.println(cnt);
            System.out.print(sb);
        } else {
            System.out.print(0);
        }
    }
}
