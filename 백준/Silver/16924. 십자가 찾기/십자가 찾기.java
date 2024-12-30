import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] Args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());


        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        char[][] board = new char[N][M];
        boolean[][] visited = new boolean[N][M];

        ArrayList<ArrayList<Integer>> answerList = new ArrayList<>();

        // 입력받기
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                board[i][j] = line.charAt(j);
            }
        }

        // 배열 탐색하면서 4방향 확인
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                int size = 0;

                if (board[i][j] == '*') {
                    for (int k = 1; ; k++) {
                        if (i - k >= 0 && j - k >= 0 && i + k < N && j + k < M) {
                            if (board[i-k][j] == '*' && board[i+k][j] == '*' && board[i][j-k] == '*' && board[i][j+k] == '*') {
                                size = k;
                            } else {
                                break;
                            }
                        } else {
                            break;
                        }
                    }
                }

                if (size > 0) {
                    visited[i][j] = true;
                    for (int k = size; k > 0; k--) {
                        answerList.add(new ArrayList<>(Arrays.asList(i+1, j+1, k)));
                        visited[i+k][j] = true;
                        visited[i-k][j] = true;
                        visited[i][j+k] = true;
                        visited[i][j-k] = true;
                    }
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == '*' && !visited[i][j]) {
                    System.out.println(-1);
                    return;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append(answerList.size()).append("\n");

        for (ArrayList<Integer> inList : answerList) {
            sb.append(inList.get(0)).append(" ").append(inList.get(1)).append(" ").append(inList.get(2)).append("\n");
        }

        System.out.println(sb);
    }
}
