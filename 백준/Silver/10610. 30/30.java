import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String N = br.readLine();
        char[] charArr = N.toCharArray();
        Arrays.sort(charArr);
        
        int total = 0;
        for (int i = N.length()-1; i >= 0; i--) {
            int num = charArr[i] - '0';
            total += num;
            sb.append(charArr[i]);
        }

        if (total % 3 != 0 || charArr[0] != '0') {
            System.out.print(-1);
        } else {
            System.out.print(sb);
        }
    }
}
