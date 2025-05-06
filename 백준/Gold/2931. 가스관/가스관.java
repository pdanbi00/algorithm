import java.io.*;
import java.util.*;
public class Main {
    static int R, C, dir, M[];
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static char board[][];
    /*
    * '|' : 세로 블럭
    * '_' : 가로 블럭
    * '+' : 십자 블럭
    * '1' : 오른쪽, 아래 블럭
    * '2' : 오른쪽, 위 블럭
    * '3' : 왼쪽, 위 블럭
    * '4' : 왼쪽, 아래 블럭
    * */
    static char[] pipes = {'|', '-', '+', '1', '2', '3', '4'};
    // 들어오는 방향에 따라 설치할 수 있는 파이프 종류
    static char[][] pipes_case = {
            {'|', '+', '4', '1'},
            {'+', '|', '3', '2'},
            {'2', '1', '-', '+'},
            {'3', '4', '+', '-'}
    };
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        board = new char[R][C];
        M = new int[2]; // 모스크바 위치

        for (int i = 0; i < R; i++) {
            board[i] = br.readLine().toCharArray();
            for (int j = 0; j < C; j++) {
                if (board[i][j] == 'M') {
                    M[0] = i;
                    M[1] = j;
                }
            }
        }

        dir = -1;
        // 모스크바에서 출발 할 수 있는지 확인
        for (int i = 0; i < 4; i++) {
            int nr = M[0] + dr[i];
            int nc = M[1] + dc[i];

            if (0 > nr || nr >= R || 0 > nc || nc >= C) {
                continue;
            }
            if (board[nr][nc] != '.') {
                dir = i;
            }

        }
        find_blank(M[0], M[1], dir);
    }
    // 중간에 끊어진 곳 찾기
    static void find_blank(int r, int c, int d) {
        int nr = r + dr[d];
        int nc = c + dc[d];

        if (board[nr][nc] == '.') {
            find_pipe(nr, nc, d);
        } else if (board[nr][nc] == '1') {
            if (d == 0) {
                d = 3;
            } else if (d == 2) {
                d = 1;
            }
            find_blank(nr, nc, d);
        } else if (board[nr][nc] == '2') {
            if (d == 1) {
                d = 3;
            } else if (d == 2) {
                d = 0;
            }
            find_blank(nr, nc, d);
        } else if (board[nr][nc] == '3') {
            if (d == 1) {
                d = 2;
            } else if (d == 3) {
                d = 0;
            }
            find_blank(nr, nc, d);
        } else if (board[nr][nc] == '4') {
            if (d == 0) {
                d = 2;
            } else if (d == 3) {
                d = 1;
            }
            find_blank(nr, nc, d);
        } else {
            find_blank(nr, nc, d);
        }
    }

        // 빈 곳에 들어가야하는 파이프 찾기
        static void find_pipe(int r, int c, int d) {
            int undir = 0;
            if (d == 0) {
                undir = 1;
            } else if (d == 1) {
                undir = 0;
            } else if (d == 2) {
                undir = 3;
            } else if (d == 3) {
                undir = 2;
            }

            Queue<Integer> q = new LinkedList<>();
            for (int i = 0; i < 4 ; i++) {
                if (i == undir) {
                    continue;
                }
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (0 > nr || R <= nr || 0 > nc || C <= nc || board[nr][nc] == '.' || board[nr][nc] == 'Z') {
                    continue;
                }

                for (int j = 0 ; j < 4 ; j++) {
                    if (pipes_case[i][j] == board[nr][nc]) {
                        q.offer(i);
                    }
                }
            }

            r++;
            c++;
            if (q.size() > 1) {
                System.out.println(r + " " + c + " " + pipes_case[d][undir]);
            } else {
                System.out.println(r + " " + c + " " + pipes_case[d][q.poll()]);
            }
        }

}
