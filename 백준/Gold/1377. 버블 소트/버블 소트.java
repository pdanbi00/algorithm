// 아이디어 : 정렬하기 전의 인덱스와 정렬한 후의 인덱스를 비교해서 가장 큰 값이 정답
import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] nums = new int[N][2];
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            nums[i][0] = num;
            nums[i][1] = i;
        }
        Arrays.sort(nums, Comparator.comparing((int[] o) -> o[0]));
        int answer = 0;
        for (int i = 0; i < N; i++) {
            int tmp = nums[i][1] - i;
            answer = Math.max(answer, tmp);
        }
        System.out.println(answer+1);
    }
}
