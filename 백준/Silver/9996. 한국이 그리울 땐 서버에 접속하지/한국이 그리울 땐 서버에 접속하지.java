import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        String target = br.readLine();
        int T = target.length();
        for (int tc = 0; tc < N; tc++) {
            String line = br.readLine();
            int L = line.length();
            if (T-1 > L) {
                sb.append("NE\n");
                continue;
            }

            boolean possible = true;

            for (int i = 0; i < T; i++) {
                if (target.charAt(i) == '*') {
                    break;
                }

                if (target.charAt(i) != line.charAt(i)) {
                    possible = false;
                    break;
                }
            }

            if (possible) {
                for (int i = 0; i < T; i++) {
                    if (target.charAt(T-1-i) == '*') {
                        break;
                    }

                    if (target.charAt(T-1-i) != line.charAt(L-1-i)) {
                        possible = false;
                        break;
                    }
                }
            }

            if (possible) {
                sb.append("DA\n");
            } else {
                sb.append("NE\n");
            }
        }
        System.out.println(sb);
    }
}