import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            int[] arr = new int[N+1];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                int rank = Integer.parseInt(st.nextToken());
                arr[rank] = Integer.parseInt(st.nextToken());
            }

            int ans = 1;
            int min = arr[1];
            for (int i = 2; i <= N; i++) {
                if (arr[i] < min) {
                    ans++;
                    min = arr[i];
                }
            }
            System.out.println(ans);
        }

    }
}