import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[] friends = new int[N];
        long[] term = new long[N-1];
        for (int i = 0; i < N; i++) {
            int f = Integer.parseInt(br.readLine());
            friends[i] = f;
            if (i != 0) {
                term[i-1] = (long) (friends[i] - friends[i-1]);
            }
        }
        Arrays.sort(term);
        Long answer = (long) N;
        if (K < N) {
            int idx = 0;
            while (N - K > 0) {
                answer += term[idx] - 1;
                idx++;
                N--;
            }

        }
        System.out.println(answer);
    }
}
