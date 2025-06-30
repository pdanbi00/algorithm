import java.io.*;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int p = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(br.readLine());

        int x = 0;
        int y = 0;
        int a = (p + t) / w; // 증가하는 부분인지 감소하는 부분인지 확인
        int b = (q + t) / h; // 증가하는 부분인지 감소하는 부분인지 확인
        if (a % 2 == 0) { // 증가하는 부분이라면
            x = (p + t) % w;
        } else { // 감소하는 부분이라면
            x = w - (p + t) % w;
        }

        if (b % 2 == 0) { // 증가하는 부분이라면
            y = (q + t) % h;
        } else { // 감소하는 부분이라면
            y = h - (q + t) % h;
        }
        System.out.println(x + " " + y);
    }
}
