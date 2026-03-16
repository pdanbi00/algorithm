import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String A = st.nextToken();
        String B = st.nextToken();

        long aTotal = 0;
        for (int i = 0; i < A.length(); i++) {
            aTotal += A.charAt(i) - '0';
        }

        long bTotal = 0;
        for (int i = 0; i < B.length(); i++) {
            bTotal += B.charAt(i) - '0';
        }
        System.out.print(aTotal * bTotal);
    }
}
