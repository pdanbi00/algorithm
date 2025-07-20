import java.io.*;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int maxLen = 0;
        char[][] board = new char[5][15];

        for (int i = 0; i < 5; i++) {
            String arr = br.readLine();
            maxLen = Math.max(maxLen, arr.length());
            for (int j = 0; j < arr.length(); j++) {
                board[i][j] = arr.charAt(j);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int j = 0; j < maxLen; j++) {
            for (int i = 0; i < 5; i++) {
                if (board[i][j] != '\0') {
                    sb.append(board[i][j]);
                }
            }
        }
        System.out.println(sb);
    }

}
