import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        char[][] board = new char[N][N];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < N; j++) {
                board[i][j] = line.charAt(j);
            }
        }
        int[] ansList = new int[N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (i != j) {
                    if (board[i][j] == 'Y') {
                        ansList[i]++;
                    } else {
                        for (int k = 0; k < N; k++) {
                            if (i != k && j != k) {
                                if (board[i][k] == 'Y' && board[j][k] == 'Y') {
                                    ansList[i]++;
                                    break;
                                }
                            }
                        }
                    }
                }
            }
        }
        int max_v = 0;
        for (int i = 0; i < N; i++) {
            if (ansList[i] > max_v) {
                max_v = ansList[i];
            }
        }
        System.out.println(max_v);

    }
}
