import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < T; tc++) {
            int N = Integer.parseInt(br.readLine());
            int[] R = new int[N];
            StringTokenizer st = new StringTokenizer(br.readLine());
            boolean possible = true;
            for (int i = 0; i < N; i++) {
                R[i] = Integer.parseInt(st.nextToken());
            }
            ArrayList<Integer> used = new ArrayList<>();
            int[] ans = new int[N];
            used.add(R[N-1] + 1);
            ans[N-1] = R[N-1] + 1;
            for (int i = N-2; i >= 0; i--) {
                int res = R[i] + 1;
                Collections.sort(used);
                for (int j : used) {
                    if (res >= j) {
                        res++;
                    } else {
                        break;
                    }
                }
                if (res > N) {
                    possible = false;
                    break;
                }

                ans[i] = res;
                used.add(res);
            }

            if (possible) {
                for (int i = 0; i < N; i++) {
                    sb.append(ans[i] + " ");
                }
                sb.append("\n");
            } else {
                sb.append("IMPOSSIBLE\n");
            }
        }
        System.out.println(sb);
    }
}
