import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
public class Main {
    static ArrayList<Integer> nums;
    static boolean[] check;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        nums = new ArrayList<>();
        check = new boolean[10];
        int num = 1;
        while (nums.size() <= 1000000) {
            if (!duplication(num)) {
                nums.add(num);
            }
            num++;
        }

        while (true) {
            int N = Integer.parseInt(br.readLine());
            if (N == 0) {
                break;
            }
            System.out.println(nums.get(N-1));
        }
    }

    static boolean duplication(int num) {
        Arrays.fill(check, false); // 매번 new 로 새로운 배열 만들면 메모리 초과
        while (num > 0) {
            int tmp = num % 10;

            if (check[tmp]) {
                return true;
            }
            check[tmp] = true;
            num /= 10;
        }
        return false;
    }
}
