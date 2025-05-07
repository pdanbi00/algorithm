import java.util.*;
import java.io.*;
public class Main {
    static List<Long> nums = new ArrayList<>();
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < 10; i++) {
            dfs(i);
        }

        Collections.sort(nums);
        if (N >= nums.size()) {
            System.out.println(-1);
        } else {
            System.out.print(nums.get(N));
        }



    }
    private static void dfs(long num) {
        nums.add(num);
        long modValue = num % 10;
        if (modValue == 0) {
            return;
        }

        for (long i = modValue-1; i >= 0; i--) {
            long newValue = num * 10 + i;
            dfs(newValue);
        }


    }
}
