import java.io.*;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] schools = new String[N+1];
        int[] next = new int[N+1];
        int[] tail = new int[N+1];

        for (int i = 1; i <= N; i++) {
            schools[i] = br.readLine();
            next[i] = i;
            tail[i] = i;
        }

        int cur = -1;

        for (int i = 0; i < N-1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int left = Integer.parseInt(st.nextToken());
            int right = Integer.parseInt(st.nextToken());

            next[tail[left]] = right;
            tail[left] = tail[right];
            cur = left;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(schools[cur]);
            cur = next[cur];
        }
        System.out.println(sb);
        br.close();
    }
}
