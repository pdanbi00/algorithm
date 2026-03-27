import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int U = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());

        StringBuilder sb = new StringBuilder();
        char[] odd = new char[] {'.', '#'};
        char[] even = new char[] {'#', '.'};

        for (int i = 0; i < U + M + D; i++) {
            if (i < U) {
                for (int j = 0; j < L + N + R; j++) {
                    if (i % 2 == 0) {
                        sb.append(even[j%2]);
                    } else {
                        sb.append(odd[j%2]);
                    }
                }
                sb.append("\n");
            } else if (i < U + M) {
                for (int j = 0; j < L; j++) {
                    if (i % 2 == 0) {
                        sb.append(even[j%2]);
                    } else {
                        sb.append(odd[j%2]);
                    }
                }
                String tmp = br.readLine();
                sb.append(tmp);
                for (int j = L+N; j < L+N+R; j++) {
                    if (i % 2 == 0) {
                        sb.append(even[j%2]);
                    } else {
                        sb.append(odd[j%2]);
                    }
                }
                sb.append("\n");
            } else {
                for (int j = 0; j < L + N + R; j++) {
                    if (i % 2 == 0) {
                        sb.append(even[j%2]);
                    } else {
                        sb.append(odd[j%2]);
                    }
                }
                sb.append("\n");
            }
        }
        System.out.print(sb);
    }
}
