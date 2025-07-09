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

        dfs(N, board, 0);
        System.out.println(ans);
    }

    static int[][] move_up(int N, int[][] board) {
        int[][] new_board = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                new_board[i][j] = board[i][j];
            }
        }

        for (int i = 1; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (new_board[i][j] != 0) {
                    int idx = i-1;
                    while (idx >= 0) {
                        if (new_board[idx][j] == 0) {
                            idx--;
                        } else {
                            break;
                        }
                    }
                    if (new_board[idx+1][j] == 0) {
                        new_board[idx+1][j] = new_board[i][j];
                        new_board[i][j] = 0;
                    }
                }
            }
        }
        return new_board;
    }

    static int[][] move_down(int N, int[][] board) {
        int[][] new_board = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                new_board[i][j] = board[i][j];
            }
        }

        for (int i = N-2; i >= 0; i--) {
            for (int j = 0; j < N; j++) {
                if (new_board[i][j] != 0) {
                    int idx = i+1;
                    while (idx < N) {
                        if (new_board[idx][j] == 0) {
                            idx++;
                        } else {
                            break;
                        }
                    }
                    if (new_board[idx-1][j] == 0) {
                        new_board[idx-1][j] = new_board[i][j];
                        new_board[i][j] = 0;
                    }
                }
            }
        }
        return new_board;
    }

    static int[][] move_right(int N, int[][] board) {
        int[][] new_board = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                new_board[i][j] = board[i][j];
            }
        }

        for (int j = N-2; j >= 0; j--) {
            for (int i = 0; i < N; i++) {
                if (new_board[i][j] != 0) {
                    int idx = j+1;
                    while (idx < N) {
                        if (new_board[i][idx] == 0) {
                            idx++;
                        } else {
                            break;
                        }
                    }
                    if (new_board[i][idx-1] == 0) {
                        new_board[i][idx-1] = new_board[i][j];
                        new_board[i][j] = 0;
                    }
                }
            }
        }
        return new_board;
    }

    static int[][] move_left(int N, int[][] board) {
        int[][] new_board = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                new_board[i][j] = board[i][j];
            }
        }

        for (int j = 1; j < N; j++) {
            for (int i = 0; i < N; i++) {
                if (new_board[i][j] != 0) {
                    int idx = j-1;
                    while (idx >= 0) {
                        if (new_board[i][idx] == 0) {
                            idx--;
                        } else {
                            break;
                        }
                    }
                    if (new_board[i][idx+1] == 0) {
                        new_board[i][idx+1] = new_board[i][j];
                        new_board[i][j] = 0;
                    }
                }
            }
        }
        return new_board;
    }

    static int[][] add_up(int N, int[][] arr) {
        for (int j = 0; j < N; j++) {
            int idx = 0;
            while (idx < N-1) {
                if (arr[idx][j] != 0 && arr[idx][j] == arr[idx+1][j]) {
                    arr[idx][j] = arr[idx][j] * 2;
                    arr[idx+1][j] = 0;
                    idx += 2;
                } else {
                    idx += 1;
                }
            }
        }
        return arr;
    }

    static int[][] add_down(int N, int[][] arr) {
        for (int j = 0; j < N; j++) {
            int idx = N-1;
            while (idx > 0) {
                if (arr[idx][j] != 0 && arr[idx][j] == arr[idx-1][j]) {
                    arr[idx][j] = arr[idx][j] * 2;
                    arr[idx-1][j] = 0;
                    idx -= 2;
                } else {
                    idx -= 1;
                }
            }
        }
        return arr;
    }

    static int[][] add_right(int N, int[][] arr) {
        for (int i = 0; i < N; i++) {
            int idx = N-1;
            while (idx > 0) {
                if (arr[i][idx] != 0 && arr[i][idx] == arr[i][idx-1]) {
                    arr[i][idx] = arr[i][idx] * 2;
                    arr[i][idx-1] = 0;
                    idx -= 2;
                } else {
                    idx -= 1;
                }
            }
        }
        return arr;
    }

    static int[][] add_left(int N, int[][] arr) {
        for (int i = 0; i < N; i++) {
            int idx = 0;
            while (idx < N-1) {
                if (arr[i][idx] != 0 && arr[i][idx] == arr[i][idx+1]) {
                    arr[i][idx] = arr[i][idx] * 2;
                    arr[i][idx+1] = 0;
                    idx += 2;
                } else {
                    idx += 1;
                }
            }
        }
        return arr;
    }

    static int[][] up(int N, int[][]board) {
        int[][] arr = new int[N][N];
        arr = move_up(N, board);
        arr = add_up(N, arr);
        arr = move_up(N, arr);
        return arr;
    }

    static int[][] down(int N, int[][]board) {
        int[][] arr = new int[N][N];
        arr = move_down(N, board);
        arr = add_down(N, arr);
        arr = move_down(N, arr);
        return arr;
    }

    static int[][] right(int N, int[][]board) {
        int[][] arr = new int[N][N];
        arr = move_right(N, board);
        arr = add_right(N, arr);
        arr = move_right(N, arr);
        return arr;
    }

    static int[][] left(int N, int[][]board) {
        int[][] arr = new int[N][N];
        arr = move_left(N, board);
        arr = add_left(N, arr);
        arr = move_left(N, arr);
        return arr;
    }

    static void dfs(int N, int[][] board, int cnt) {
        if (cnt == 5) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    ans = Math.max(ans, board[i][j]);
                }
            }
            return;
        }

        int[][] new_arr = new int[N][N];

        new_arr = up(N, board);
        dfs(N, new_arr, cnt+1);

        new_arr = down(N, board);
        dfs(N, new_arr, cnt+1);

        new_arr = right(N, board);
        dfs(N, new_arr, cnt+1);

        new_arr = left(N, board);
        dfs(N, new_arr, cnt+1);
    }
}
