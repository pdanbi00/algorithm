import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int[] nums = new int[N];
            for (int i = 0; i < N; i++) {
                int n = Integer.parseInt(st.nextToken());
                nums[i] = n;
            }
            Arrays.sort(nums);
            int[] ansList = new int[N];
            Arrays.fill(ansList, Integer.MAX_VALUE);
            for (int i = 0; i < N; i++) {
                int tmp = 0;
                for (int j = i-1; j >= 0; j--) {
                    tmp += nums[i] - nums[j];
                    ansList[i-j] = Math.min(ansList[i-j], tmp);
                }
            }
            int ans = 0;
            for (int i = 1; i < N; i++) {
                ans += ansList[i];
            }
            System.out.println(ans);
        }
    }
}
