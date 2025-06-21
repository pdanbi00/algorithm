import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < T; tc++) {
            int N = Integer.parseInt(br.readLine());
            int[] R = new int[N];
            StringTokenizer st = new StringTokenizer(br.readLine());
            boolean possible = true;
            for (int i = 0; i < N; i++) {
                R[i] = Integer.parseInt(st.nextToken());
                if (R[i] > i) {
                    possible = false;
                }
            }
            int num = 1;
            if (possible) {
                int[] answer = new int[N];
                boolean[] visited = new boolean[N];
                while (num <= N) {
                    int zero_idx = -1;
                    for (int i = 0; i < N; i++) {
                        if (R[i] == 0 && !visited[i]) {
                            zero_idx = i;
                        }
                    }
                    if (zero_idx == -1) {
                        break;
                    }
                    answer[zero_idx] = num;
                    num++;
                    visited[zero_idx] = true;

                    for (int i = zero_idx + 1; i < N; i++) {
                        if (R[i] != 0) {
                            R[i] -= 1;
                        }
                    }

                }
                for (int i = 0; i < N; i++) {
                    System.out.print(answer[i] + " ");
                }
                System.out.println("");
            } else {
                System.out.println("IMPOSSIBLE");
            }
        }
    }
}
