import java.io.*;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        while (T > 0) {
            T -= 1;
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());

            int max = Math.max(a, b);
            int min = Math.min(a, b);

            int limit = s / max;
            boolean[] flag = new boolean[min];
            boolean possible = false;

            for (int i = limit; i >= 0; i--) {
                int remain = s - i * max;
                int mod = remain % min;

                if (flag[mod]) {
                    break;
                }
                flag[mod] = true;
                if (mod == 0) {
                    possible = true;
                    if (max == a) {
                        sb.append(i + " " + remain / min + "\n");
                    } else {
                        sb.append(remain / min + " " + i + "\n");
                    }
                }
            }

            if (!possible) {
                sb.append("Impossible\n");
            }
        }
        System.out.println(sb);
    }
}
