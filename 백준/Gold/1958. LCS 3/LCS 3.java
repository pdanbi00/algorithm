import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String first = br.readLine();
        String second = br.readLine();
        String third = br.readLine();

        int[][][] LCS = new int[first.length()+1][second.length()+1][third.length()+1];
        for (int i = 1; i < first.length()+1; i++) {
            for (int j = 1; j < second.length()+1; j++) {
                for (int k = 1; k < third.length()+1; k++) {
                    if (first.charAt(i-1) == second.charAt(j-1) && second.charAt(j-1) == third.charAt(k-1)) {
                        LCS[i][j][k] = LCS[i-1][j-1][k-1] + 1;
                    } else {
                        LCS[i][j][k] = Math.max(Math.max(LCS[i-1][j][k], LCS[i][j-1][k]), LCS[i][j][k-1]);
                    }
                }
            }
        }

        System.out.println(LCS[first.length()][second.length()][third.length()]);
    }
}
