import java.io.*;
import java.util.StringTokenizer;
import java.util.Deque;
import java.util.LinkedList;
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        Deque<Integer> nums = new LinkedList<>();
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = 1; i <= N; i++) {
            nums.add(i);
        }
        int idx = 0;
        while (idx < K-1) {
            int tmp = nums.pollFirst();
            nums.addLast(tmp);
            idx++;
        }
        int cnt = 0;
        int dir = 0;
        while (!nums.isEmpty()) {
            int tmp = nums.pollFirst();
            answer.add(tmp);
            cnt++;
            if (cnt % M == 0) {
                dir++;
            }
            if (dir % 2 == 0) { // 오른쪽 방향
                idx = 0;
                while (idx < K-1 && !nums.isEmpty()) {
                    tmp = nums.pollFirst();
                    nums.addLast(tmp);
                    idx++;
                }
            } else {
                idx = 0;
                while (idx < K && !nums.isEmpty()) {
                    tmp = nums.pollLast();
                    nums.addFirst(tmp);
                    idx++;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < answer.size(); i++) {
            sb.append(answer.get(i)).append("\n");
        }
        System.out.print(sb);
    }
}
