import java.io.*;
import java.util.StringTokenizer;
import java.util.Set;
import java.util.HashSet;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Set<String> S = new HashSet<>();
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            S.add(line);
        }

        int answer = 0;
        for (int i = 0; i < M; i++) {
            String line = br.readLine();
            if (S.contains(line)) {
                answer++;
            }
        }
        System.out.println(answer);
    }
}
