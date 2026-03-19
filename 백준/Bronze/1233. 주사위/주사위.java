import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Map;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int s1 = Integer.parseInt(st.nextToken());
        int s2 = Integer.parseInt(st.nextToken());
        int s3 = Integer.parseInt(st.nextToken());

        int ans = s1 * s2 * s3;
        int maxCnt = 0;
        Map<Integer, Integer> cnt = new HashMap<>();

        for (int i = 1; i <= s1; i++) {
            for (int j = 1; j <= s2; j++) {
                for (int k = 1; k <= s3; k++) {
                    int sum = i + j + k;

                    if (cnt.containsKey(sum)) {
                        int tmp = cnt.get(sum);
                        cnt.put(sum, tmp+1);
                        maxCnt = Math.max(maxCnt, tmp+1);
                    } else {
                        cnt.put(sum, 1);
                        maxCnt = Math.max(maxCnt, 1);
                    }
                }
            }
        }

        for (int k : cnt.keySet()) {
            if (cnt.get(k) == maxCnt) {
                if (ans > k) {
                    ans = k;
                }
            }
        }
        System.out.print(ans);
    }
}
