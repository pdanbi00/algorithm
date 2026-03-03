import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int[] flipped = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            flipped[i] = Integer.parseInt(st.nextToken());
        }

        int time = 0;
        int up = 0, down = s;
        int tmp;
        for (int i = 0; i < n-1; i++) {
            tmp = up;
            up = down;
            down = tmp;

            tmp = flipped[i+1] - flipped[i];
            if (tmp > up) {
                up = 0;
                down = s;
            } else {
                up -= tmp;
                down += tmp;
            }
        }
        time = flipped[n-1] + down;
        if (time <= t) {
            time = 0;
        } else {
            time -= t;
        }
        System.out.print(time);
    }
}