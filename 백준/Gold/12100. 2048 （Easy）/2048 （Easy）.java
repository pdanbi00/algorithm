import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
    static int N, ans;
    static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        ans = 0;

        game(0);
        System.out.println(ans);
    }

    public static void game(int cnt) {
        if (cnt == 5) {
            findMax();
            return;
        }
        int[][] copy = new int[N][N];
        for (int i = 0; i < N; i++) {
            copy[i] = board[i].clone();
        }
        for (int i = 0; i < 4; i++) {
            move(i);
            game(cnt+1);
            for (int a = 0; a < N; a++) {
                board[a] = copy[a].clone();
            }
        }
    }

    public static void move(int dir) {
        switch (dir) {
            // 위로 밀기
            case 0:
                for (int j = 0; j < N; j++) {
                    int idx = 0; // 값 넣을 위치
                    int block = 0; // 최근 블록 값
                    for (int i = 0; i < N; i++) {
                        // 현재 블록의 값이 0이 아니라면
                        if (board[i][j] != 0) {
                            // 최근 블록 값이랑 현재 블록 값이 같다면
                            if (board[i][j] == block) {
                                // 블록 합쳐짐
                                board[idx-1][j] = block * 2;
                                // 블록 합쳐졌으니깐 0으로 갱신
                                block = 0;
                                // 값 합쳤으니깐 현재 블록 값은 0
                                board[i][j] = 0;

                            }
                            // 최근 블록 값이랑 현재 블록 값이 다르면
                            else {
                                // 블록 변수 값을 현재 블록 값으로 갱신
                                block = board[i][j];
                                // 현재 블록 값을 0으로 바꿔줌.
                                board[i][j] = 0;
                                // 값 넣을 위치에 최근 블록 값 넣기
                                board[idx][j] = block;
                                // 값 넣을 위치 변경
                                idx++;
                            }
                        }
                    }
                }
                break;
            // 아래로 밀기
            case 1:
                for (int j = 0; j < N; j++) {
                    int idx = N-1; // 값 넣을 위치
                    int block = 0; // 최근 블록 값
                    for (int i = N-1; i >= 0; i--) {
                        // 현재 블록의 값이 0이 아니라면
                        if (board[i][j] != 0) {
                            // 최근 블록 값이랑 현재 블록 값이 같다면
                            if (board[i][j] == block) {
                                // 블록 합쳐짐
                                board[idx+1][j] = block * 2;
                                // 블록 합쳐졌으니깐 0으로 갱신
                                block = 0;
                                // 값 합쳤으니깐 현재 블록 값은 0
                                board[i][j] = 0;

                            }
                            // 최근 블록 값이랑 현재 블록 값이 다르면
                            else {
                                // 블록 변수 값을 현재 블록 값으로 갱신
                                block = board[i][j];
                                // 현재 블록 값을 0으로 바꿔줌.
                                board[i][j] = 0;
                                // 값 넣을 위치에 최근 블록 값 넣기
                                board[idx][j] = block;
                                // 값 넣을 위치 변경
                                idx--;
                            }
                        }
                    }
                }
                break;
            // 왼쪽으로 밀기
            case 2:
                for (int i = 0; i < N; i++) {
                    int idx = 0; // 값 넣을 위치
                    int block = 0; // 최근 블록 값
                    for (int j = 0; j < N; j++) {
                        // 현재 블록의 값이 0이 아니라면
                        if (board[i][j] != 0) {
                            // 최근 블록 값이랑 현재 블록 값이 같다면
                            if (board[i][j] == block) {
                                // 블록 합쳐짐
                                board[i][idx-1] = block * 2;
                                // 블록 합쳐졌으니깐 0으로 갱신
                                block = 0;
                                // 값 합쳤으니깐 현재 블록 값은 0
                                board[i][j] = 0;

                            }
                            // 최근 블록 값이랑 현재 블록 값이 다르면
                            else {
                                // 블록 변수 값을 현재 블록 값으로 갱신
                                block = board[i][j];
                                // 현재 블록 값을 0으로 바꿔줌.
                                board[i][j] = 0;
                                // 값 넣을 위치에 최근 블록 값 넣기
                                board[i][idx] = block;
                                // 값 넣을 위치 변경
                                idx++;
                            }
                        }
                    }
                }
                break;
            // 오른쪽으로 밀기
            case 3:
                for (int i = 0; i < N; i++) {
                    int idx = N-1; // 값 넣을 위치
                    int block = 0; // 최근 블록 값
                    for (int j = N-1; j >= 0; j--) {
                        // 현재 블록의 값이 0이 아니라면
                        if (board[i][j] != 0) {
                            // 최근 블록 값이랑 현재 블록 값이 같다면
                            if (board[i][j] == block) {
                                // 블록 합쳐짐
                                board[i][idx+1] = block * 2;
                                // 블록 합쳐졌으니깐 0으로 갱신
                                block = 0;
                                // 값 합쳤으니깐 현재 블록 값은 0
                                board[i][j] = 0;

                            }
                            // 최근 블록 값이랑 현재 블록 값이 다르면
                            else {
                                // 블록 변수 값을 현재 블록 값으로 갱신
                                block = board[i][j];
                                // 현재 블록 값을 0으로 바꿔줌.
                                board[i][j] = 0;
                                // 값 넣을 위치에 최근 블록 값 넣기
                                board[i][idx] = block;
                                // 값 넣을 위치 변경
                                idx--;
                            }
                        }
                    }
                }
                break;
        }
    }
    public static void findMax() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                ans = Math.max(ans, board[i][j]);
            }
        }
    }
}