import java.io.*;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.Stack;
import java.util.Queue;
public class Main {
    static int N, K;
    static int[][] board; // 각 칸이 무슨색인지 표현하는 변수
    static int[] dr = {0, 0, 0, -1, 1};
    static int[] dc = {0, 1, -1, 0, 0};
    static int answer;
    static boolean end;
    static Map<Integer, int[]> piecesMap; // 각 말에 대한 행, 열, 방향에 대한 정보를 담은 맵
    static Stack<Integer>[][] pieces; // 각 행과 열에 위치한 말들 표현하는 변수
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        board = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        pieces = new Stack[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                pieces[i][j] = new Stack<>();
            }
        }

        piecesMap = new HashMap<>();
        for (int i = 1; i <= K; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            piecesMap.put(i, new int[] {r-1, c-1, d}); // 행, 열, 방향
            pieces[r-1][c-1].add(i);
        }
        answer = 1;
        end = false;
        while (answer <= 1000) {
            game();
            if (end) {
                break;
            }
            answer++;
        }
        if (end) {
            System.out.println(answer);
        } else {
            System.out.println(-1);
        }

    }
    static void game() {
        // 한 턴 동안 이뤄지는 일
        // 1번 말부터 K번 말까지 순서대로 이동. 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동함.
        // 말이 4개이상 쌓이면 게임은 종료됨
        boolean over = false;
        for (int i = 1; i <= K; i++) {
            int[] data = piecesMap.get(i);
            int r = data[0];
            int c = data[1];
            int dir = data[2];

            int nr = r + dr[dir];
            int nc = c + dc[dir];
            if (0 <= nr && nr < N && 0 <= nc && nc < N) {
                if (board[nr][nc] == 0) { // 1. 이동하려는 칸이 흰색이면 이동.
                    Stack<Integer> tmp = new Stack<>();
                    while (!pieces[r][c].isEmpty()) {
                        int now = pieces[r][c].pop();
                        tmp.add(now);
                        if (now == i) {
                            break;
                        }
                    }
                    while (!tmp.isEmpty()) {
                        int num = tmp.pop();
                        // pieces[nr][nc]로 말 이동시키기
                        pieces[nr][nc].add(num);
                        if (pieces[nr][nc].size() >= 4) {
                            over = true;
                            end = true;
                            break;
                        }
                        // piecesMap에서 상태 업데이트
                        int[] cur = piecesMap.get(num);
                        piecesMap.put(num, new int[]{nr, nc, cur[2]});
                    }
                    if (over) {
                        break;
                    }
                } else if (board[nr][nc] == 1) { // 2. 이동하려는 칸이 빨간색이면 이동한 후에 A번 말부터 그 위의 모든 말의 순서를 반대로 바꿈
                    while (!pieces[r][c].isEmpty()) {
                        int now = pieces[r][c].pop();
                        // pieces[nr][nc]로 말 이동시키기
                        pieces[nr][nc].add(now);
                        if (pieces[nr][nc].size() >= 4) {
                            over = true;
                            end = true;
                            break;
                        }
                        // piecesMap에서 상태 업데이트
                        int[] cur = piecesMap.get(now);
                        piecesMap.put(now, new int[]{nr, nc, cur[2]});
                        if (now == i) {
                            break;
                        }
                    }
                    if (over) {
                        break;
                    }
                } else if (board[nr][nc] == 2) { // 3. 이동하려는 칸이 파란색인 경우 A번 말의 이동 방향을 반대로. 근데 반대방향으로 바꾼 후에 이동하려는 칸도 파란색이면 가만히 있음.
                    if (dir == 1) {
                        nr = r + dr[2];
                        nc = c + dc[2];
                        dir = 2;
                    } else if (dir == 2) {
                        nr = r + dr[1];
                        nc = c + dc[1];
                        dir = 1;
                    } else if (dir == 3) {
                        nr = r + dr[4];
                        nc = c + dc[4];
                        dir = 4;
                    } else if (dir == 4) {
                        nr = r + dr[3];
                        nc = c + dc[3];
                        dir = 3;
                    }
                    if (0 <= nr && nr < N && 0 <= nc && nc < N) {
                        if (board[nr][nc] == 0) { // 새로 이동하려는 칸이 흰색이면 이동.
                            Stack<Integer> tmp = new Stack<>();
                            while (!pieces[r][c].isEmpty()) {
                                int now = pieces[r][c].pop();
                                tmp.add(now);
                                if (now == i) {
                                    break;
                                }
                            }
                            while (!tmp.isEmpty()) {
                                int num = tmp.pop();
                                // pieces[nr][nc]로 말 이동시키기
                                pieces[nr][nc].add(num);
                                if (pieces[nr][nc].size() >= 4) {
                                    over = true;
                                    end = true;
                                    break;
                                }
                                // piecesMap에서 상태 업데이트
                                int[] cur = piecesMap.get(num);
                                if (num == i) {
                                    piecesMap.put(num, new int[]{nr, nc, dir});
                                } else {
                                    piecesMap.put(num, new int[]{nr, nc, cur[2]});
                                }
                            }
                            if (over) {
                                break;
                            }
                        } else if (board[nr][nc] == 1) { // 새로 이동하려는 칸이 빨간색이면 이동한 후에 A번 말부터 그 위의 모든 말의 순서를 반대로 바꿈
                            while (!pieces[r][c].isEmpty()) {
                                int now = pieces[r][c].pop();
                                // pieces[nr][nc]로 말 이동시키기
                                pieces[nr][nc].add(now);
                                if (pieces[nr][nc].size() >= 4) {
                                    over = true;
                                    end = true;
                                    break;
                                }
                                // piecesMap에서 상태 업데이트
                                int[] cur = piecesMap.get(now);

                                if (now == i) {
                                    piecesMap.put(now, new int[]{nr, nc, dir});
                                    break;
                                } else {
                                    piecesMap.put(now, new int[]{nr, nc, cur[2]});
                                }
                            }
                            if (over) {
                                break;
                            }
                        } else if (board[nr][nc] == 2) { // 근데 반대방향으로 바꾼 후에 이동하려는 칸도 파란색이면 가만히 있음.
                            // 현재 말만 piecesMap에서 상태 업데이트
                            piecesMap.put(i, new int[]{r, c, dir});
                        }
                    }
                }

            } else {
                // 4. 체스판 벗어나는 경우도 파란색과 같이 이동 방향을 반대로 함. 반대 방향도 파란색이면 가만히
                if (dir == 1) {
                    nr = r + dr[2];
                    nc = c + dc[2];
                    dir = 2;
                } else if (dir == 2) {
                    nr = r + dr[1];
                    nc = c + dc[1];
                    dir = 1;
                } else if (dir == 3) {
                    nr = r + dr[4];
                    nc = c + dc[4];
                    dir = 4;
                } else if (dir == 4) {
                    nr = r + dr[3];
                    nc = c + dc[3];
                    dir = 3;
                }

                if (board[nr][nc] == 0) { // 새로 이동하려는 칸이 흰색이면 이동.
                    Stack<Integer> tmp = new Stack<>();
                    while (!pieces[r][c].isEmpty()) {
                        int now = pieces[r][c].pop();
                        tmp.add(now);
                        if (now == i) {
                            break;
                        }
                    }
                    while (!tmp.isEmpty()) {
                        int num = tmp.pop();
                        // pieces[nr][nc]로 말 이동시키기
                        pieces[nr][nc].add(num);
                        if (pieces[nr][nc].size() >= 4) {
                            over = true;
                            end = true;
                            break;
                        }
                        // piecesMap에서 상태 업데이트
                        int[] cur = piecesMap.get(num);
                        if (num == i) {
                            piecesMap.put(num, new int[]{nr, nc, dir});
                        } else {
                            piecesMap.put(num, new int[]{nr, nc, cur[2]});
                        }
                    }
                    if (over) {
                        break;
                    }
                } else if (board[nr][nc] == 1) { // 새로 이동하려는 칸이 빨간색이면 이동한 후에 A번 말부터 그 위의 모든 말의 순서를 반대로 바꿈
                    while (!pieces[r][c].isEmpty()) {
                        int now = pieces[r][c].pop();
                        // pieces[nr][nc]로 말 이동시키기
                        pieces[nr][nc].add(now);
                        if (pieces[nr][nc].size() >= 4) {
                            over = true;
                            end = true;
                            break;
                        }
                        // piecesMap에서 상태 업데이트
                        int[] cur = piecesMap.get(now);

                        if (now == i) {
                            piecesMap.put(now, new int[]{nr, nc, dir});
                            break;
                        } else {
                            piecesMap.put(now, new int[]{nr, nc, cur[2]});
                        }
                    }
                    if (over) {
                        break;
                    }
                } else if (board[nr][nc] == 2) { // 근데 반대방향으로 바꾼 후에 이동하려는 칸도 파란색이면 가만히 있음.
                    // 현재 말만 piecesMap에서 상태 업데이트
                    piecesMap.put(i, new int[]{r, c, dir});
                }
            }
        }
    }
}
