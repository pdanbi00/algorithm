import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] board = new int[B][A];
        for (int i = 0; i < B; i++) {
            Arrays.fill(board[i], -1);
        }
        Map<Integer, int[]> robots = new HashMap<>();
        int[] dr = {-1, 0, 1, 0};
        int[] dc = {0, 1, 0, -1};

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            int c = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            char d = st.nextToken().charAt(0);
            int dir = 0;
            board[B-(r-1)-1][c-1] = i;
            if (d == 'N') {
                dir = 0;
            } else if (d == 'E') {
                dir = 1;
            } else if (d == 'S') {
                dir = 2;
            } else if (d == 'W') {
                dir = 3;
            }

            int[] tmp = {B-(r-1)-1, c-1, dir};
            robots.put(i, tmp);
        }

        boolean possible = true;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());
            char command = st.nextToken().charAt(0);
            int cnt = Integer.parseInt(st.nextToken());
            int[] tmp = robots.get(num);
            int r = tmp[0];
            int c = tmp[1];
            int d = tmp[2];
            if (command == 'L') {
                d = (d + (3 * cnt)) % 4;
                int[] arr = {r, c, d};
                robots.put(num, arr);
            } else if (command == 'R') {
                d = (d + cnt) % 4;
                int[] arr = {r, c, d};
                robots.put(num, arr);
            } else {
                while (cnt > 0) {
                    cnt -= 1;
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (0 <= nr && nr < B && 0 <= nc && nc < A) {
                        if (board[nr][nc] != -1) {
                            System.out.println("Robot " + num + " crashes into robot " + board[nr][nc]);
                            possible = false;
                            break;
                        } else {
                            int[] arr = {nr, nc, d};
                            robots.put(num, arr);
                            board[r][c] = -1;
                            board[nr][nc] = num;
                            r = nr;
                            c = nc;
                        }
                    } else {
                        System.out.println("Robot " + num + " crashes into the wall");
                        possible = false;
                        break;
                    }
                }
            }
            if (!possible) {
                break;
            }

        }
        if (possible) {
            System.out.println("OK");
        }

    }
}
