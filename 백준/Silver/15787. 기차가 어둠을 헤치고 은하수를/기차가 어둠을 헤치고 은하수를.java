import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Set;
import java.util.HashSet;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] train = new int[N];

        int a, b, c;
        int defaultNum = (int) Math.pow(2, 20);
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            if (a == 1) {
                c = Integer.parseInt(st.nextToken());
                train[b-1] = (defaultNum>>c)|train[b-1];
            } else if (a == 2) {
                c = Integer.parseInt(st.nextToken());
                train[b-1] = (~(defaultNum>>c))&train[b-1];
            } else if (a == 3) {
                train[b-1] = train[b-1]>>1;
            } else {
                train[b-1] = (int) ((train[b-1]<<1)%defaultNum);
            }
        }

        Set<Integer> milkyWay = new HashSet<>();
        for (int i = 0; i < N; i++) {
            milkyWay.add(train[i]);
        }
        System.out.print(milkyWay.size());
    }
}