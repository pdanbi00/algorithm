import java.io.*;
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

        System.out.println(compression(board));
    }

    static String compression(char[][] arr) {
        if (arr.length == 0) {
            return String.valueOf(arr[0]);
        }

        int l = arr.length;
        // arr의 모든 값이 같다면 해당 값 return
        char c = arr[0][0];
        boolean possible = true;
        for (int i = 0; i < l; i++) {
            for (int j = 0; j < l; j++) {
                if (arr[i][j] != c) {
                    possible = false;
                    break;
                }
            }
            if (!possible) {
                break;
            }
        }

        if (possible) {
            return String.valueOf(c);
        }

        String result = "";

        for (int k = 0; k < l; k += l/2) {
            for (int p = 0; p < l; p += l/2) {
                char[][] tmp = new char[l/2][l/2];
                for (int i = 0; i < l/2; i++) {
                    for (int j = 0; j < l/2; j++) {
                        tmp[i][j] = arr[k+i][p+j];
                    }
                }
                result += compression(tmp);
            }
        }
        return "(" + result + ")";
    }
}
