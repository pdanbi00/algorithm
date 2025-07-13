import java.io.*;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;
import java.util.Set;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        boolean possible = true;
        char[] answer = new char[N];
        int idx = 0;
        Set<Character> charSet = new HashSet<>();
        Arrays.fill(answer, '?');
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int cnt = Integer.parseInt(st.nextToken());
            char alpha = st.nextToken().charAt(0);
            idx += cnt;
            if (answer[idx % N] == '?') {
                if (!charSet.contains(alpha)) {
                    answer[idx % N] = alpha;
                    charSet.add(alpha);
                } else {
                    possible = false;
                    break;
                }
            } else if (answer[idx % N] != alpha) {
                possible = false;
                break;
            }
        }

        if (!possible) {
            System.out.println('!');
        } else {
            String ans = "";
            for (int i = 0; i < N; i++) {
                ans += answer[(idx + (N-i)) % N];
            }
            System.out.println(ans);
        }
    }
}
