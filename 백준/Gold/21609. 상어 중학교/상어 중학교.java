import java.io.*;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;
public class Main {
    static int N, M;
    static int[][] board;
    static ArrayList<block> blockGroup; // 가장 큰 블록 그룹에 속한 블록들
    static int rainbowCnt; // 무지개 블럭 개수
    static int stdR; // 기준 블록 행
    static int stdC; // 기준 블록 열
    static int score; // 획득한 점수
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        while (true) {
            blockGroup = new ArrayList<>();
            rainbowCnt = 0;
            stdR = -1;
            stdC = -1;
            find();
            if (blockGroup.isEmpty()) {
                break;
            }
            remove();
            gravity();
            board = rotation();
            gravity();
        }
        System.out.println(score);

    }
    // 크기가 가장 큰 블록 찾는 함수
    // 비교 기준 : 블록 총 개수 -> 포함된 무지개 블록 수 -> 기준 블록의 행이 가장 큰 것 -> 기준 블록의 열이 가장 큰 것
    static void find() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] > 0) {
                    int color = board[i][j];
                    int stR = i; // 기준 블럭 행
                    int stC = j; // 기준 블럭 열
                    int rainbow = 0;
                    ArrayList<block> blocks = new ArrayList<>();
                    Queue<block> q = new LinkedList<>();
                    boolean[][] visited = new boolean[N][N];
                    q.add(new block(i, j));
                    visited[i][j] = true;
                    blocks.add(new block(i, j));
                    while (!q.isEmpty()) {
                        block cur = q.poll();
                        for (int k = 0; k < 4; k++) {
                            int nr = cur.r + dr[k];
                            int nc = cur.c + dc[k];
                            if (0 <= nr && nr < N && 0 <= nc && nc < N) {
                                if ((board[nr][nc] == color || board[nr][nc] == 0) && !visited[nr][nc]) {
                                    q.add(new block(nr, nc));
                                    visited[nr][nc] = true;
                                    blocks.add(new block(nr, nc));
                                    if (board[nr][nc] == color) {
                                        if (nr < stR) {
                                            stR = nr;
                                            stC = nc;
                                        } else if (nr == stR) {
                                            if (nc < stC) {
                                                stC = nc;
                                            }
                                        }
                                    } else if (board[nr][nc] == 0) {
                                        rainbow += 1;
                                    }
                                }
                            }
                        }
                    }
                    if (blocks.size() >= 2) {
                        if (blocks.size() > blockGroup.size()) {
                            blockGroup = blocks;
                            rainbowCnt = rainbow;
                            stdR = stR;
                            stdC = stC;

                        } else if (blocks.size() == blockGroup.size()) {
                            if (rainbow > rainbowCnt) {
                                blockGroup = blocks;
                                rainbowCnt = rainbow;
                                stdR = stR;
                                stdC = stC;
                            } else if (rainbow == rainbowCnt) {
                                if (stR > stdR) {
                                    blockGroup = blocks;
                                    rainbowCnt = rainbow;
                                    stdR = stR;
                                    stdC = stC;
                                } else if (stR == stdR) {
                                    if (stC > stdC) {
                                        blockGroup = blocks;
                                        rainbowCnt = rainbow;
                                        stdR = stR;
                                        stdC = stC;
                                    }
                                }
                            }
                        }
                    }

                }
            }
        }
    }

    // 블록 제거 함수 : board값을 -2로 바꾸기
    // find 에서 찾은 블록 그룹의 모든 블록을 제거. 제거한 블록 그룹에 호팜된 블록의 수의 제곱 만큼 점수 획득
    static void remove() {
        score += blockGroup.size() * blockGroup.size();
        for (block now : blockGroup) {
            board[now.r][now.c] = -2;
        }
    }

    // 중력 함수
    static void gravity() {
        for (int j = 0; j < N; j++) {
            for (int i = N-2; i >= 0; i--) {
                if (board[i][j] >= 0) {
                    int r = i;
                    while (r < N-1) {
                        if (r + 1 < N && board[r+1][j] == -2) {
                            board[r+1][j] = board[r][j];
                            board[r][j] = -2;
                            r += 1;
                        } else {
                            break;
                        }
                    }
                }
            }
        }

    }

    // 격자 반시계 방향 회전 함수
    static int[][] rotation() {
        int[][] arr = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = board[j][N-1-i];
            }
        }
        return arr;
    }
}

class block {
    int r;
    int c;

    public block(int r, int c) {
        this.r = r;
        this.c = c;
    }
}