import java.io.*;
import java.util.StringTokenizer;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        // 이분탐색
        for (int tc = 0; tc < T; tc++) {
            int N = Integer.parseInt(br.readLine());
            int[] nums1 = new int[N];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                int num = Integer.parseInt(st.nextToken());
                nums1[i] = num;
            }
            Arrays.sort(nums1);

            int M = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < M; i++) {
                int num = Integer.parseInt(st.nextToken());
                sb.append(binarySearch(0, N-1, nums1, num)).append("\n");
            }
        }
        System.out.println(sb);
    }

    static int binarySearch(int s, int e, int[] nums, int num) {
        while (s <= e) {
            int mid = (s + e) / 2;
            if (nums[mid] == num) {
                return 1;
            } else if (nums[mid] < num) {
                s = mid + 1;
            } else {
                e = mid - 1;
            }
        }
        return 0;
    }
}