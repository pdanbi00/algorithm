import java.io.*;
import java.util.StringTokenizer;
import java.util.Map;
import java.util.HashMap;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int aCnt = Integer.parseInt(st.nextToken());
        int bCnt = Integer.parseInt(st.nextToken());
        Map<Integer, Integer> nums = new HashMap<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < aCnt; i++) {
            int num = Integer.parseInt(st.nextToken());
            if (nums.containsKey(num)) {
                nums.put(num, nums.get(num) + 1);
            } else {
                nums.put(num, 1);
            }
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < bCnt; i++) {
            int num = Integer.parseInt(st.nextToken());
            if (nums.containsKey(num)) {
                nums.put(num, nums.get(num) + 1);
            } else {
                nums.put(num, 1);
            }
        }
        int answer = 0;
        for (int k : nums.keySet()) {
            if (nums.get(k) == 1) {
                answer++;
            }
        }

        System.out.println(answer);
    }
}
