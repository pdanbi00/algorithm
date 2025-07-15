import java.io.*;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] nums = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        ArrayList<Integer> sortedNum = new ArrayList<>();
        int S = Integer.parseInt(br.readLine());
        int cnt = 0;
        while (S > 0) {
            if (sortedNum.size() == N) {
                break;
            }
            if (S == 1) {
                for (int i = cnt; i < N-1; i++) {
                    if (nums[i] < nums[i+1]) {
                        int tmp = nums[i];
                        nums[i] = nums[i+1];
                        nums[i+1] = tmp;
                        break;
                    }
                }
                break;
            }
            int[][] numsIdx = new int[N-cnt][2];
            for (int i = cnt; i < N; i++) {
                numsIdx[i-cnt][0] = nums[i];
                numsIdx[i-cnt][1] = i;
            }
            Arrays.sort(numsIdx, (o1, o2 )-> o2[0] - o1[0]);
            for (int[] num : numsIdx) {
                if (num[1] - cnt <= S) {
                    for (int j = num[1]; j > cnt; j--) {
                        int tmp = nums[j];
                        nums[j] = nums[j-1];
                        nums[j-1] = tmp;
                    }
                    S -= num[1] - cnt;
                    sortedNum.add(num[0]);
                    break;
                }
            }
            cnt++;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(nums[i]).append(" ");
        }
        System.out.println(sb);
    }
}
