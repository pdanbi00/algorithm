import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        int maxV = 0;

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            maxV = Math.max(maxV, arr[i]);
        }

        int[] answer = new int[N+1];
        int[] pos = new int[maxV+1];
        for (int i = 0; i < N; i++) {
            pos[arr[i]] = i+1;
        }

        for (int mod : arr) {
            for (int i = mod*2; i <= maxV; i += mod) {
                if (pos[i] != 0) {
                    answer[pos[mod]]++;
                    answer[pos[i]]--;
                }
            }
        }
        for (int i = 1; i <= N; i++) {
            sb.append(answer[i]).append(" ");
        }
        System.out.print(sb);
    }
}
