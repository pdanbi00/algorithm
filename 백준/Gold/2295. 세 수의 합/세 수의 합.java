import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(nums);

        // 두 숫자의 합 배열 만들기
        Set<Integer> nums_sum = new HashSet<>();
        for (int i = 0; i < N; i++) {
            for (int j = i; j < N; j++) {
                nums_sum.add(nums[i] + nums[j]);
            }
        }

        int answer = 0;
        boolean find = false;
        for (int i = N-1; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                int tmp = nums[i] - nums[j];
                if (nums_sum.contains(tmp)) {
                    answer = nums[i];
                    find = true;
                    break;
                }
            }
            if (find) {
                break;
            }
        }

        System.out.print(answer);
    }
}
