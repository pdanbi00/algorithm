import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());
        
        int[] front = new int[t];
        int[] back = new int[n-t];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            if (i < t) {
                front[i] = Integer.parseInt(st.nextToken());
            } else {
                back[i-t] = Integer.parseInt(st.nextToken());
            }
        }

        Arrays.sort(front);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            sb.append(front[i]).append(" ");
        }
        for (int i = 0; i < n-t; i++) {
            sb.append(back[i]).append(" ");
        }
        System.out.print(sb);
    }
}
