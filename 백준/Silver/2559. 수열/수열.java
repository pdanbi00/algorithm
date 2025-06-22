import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[] temperature = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            temperature[i] = Integer.parseInt(st.nextToken());
            if (i != 0) {
                temperature[i] += temperature[i-1];
            }
        }
        int max_v = temperature[K-1];
        for (int i = K; i < N; i++) {
            int temp = temperature[i] - temperature[i-K];
            max_v = Integer.max(max_v, temp);
        }
        System.out.println(max_v);
    }
}
