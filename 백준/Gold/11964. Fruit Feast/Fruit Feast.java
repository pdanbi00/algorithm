import java.io.*;
import java.util.Set;
import java.util.HashSet;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    static int T, A, B;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        T = Integer.parseInt(st.nextToken());
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {A, 0});
        q.add(new int[] {B, 0});
        int answer = 0;
        Set<Integer> nums = new HashSet<>();
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            answer = Math.max(answer, cur[0]);
            int tmp = cur[0] + A;
            if (!nums.contains(tmp)) {
                if (tmp <= T) {
                    if (tmp == T) {
                        answer = T;
                        break;
                    } else {
                        q.add(new int[] {tmp, cur[1]});
                        nums.add(tmp);
                    }
                }
            }

            tmp = cur[0] + B;
            if (!nums.contains(tmp)) {
                if (tmp <= T) {
                    if (tmp == T) {
                        answer = T;
                        break;
                    } else {
                        q.add(new int[] {tmp, cur[1]});
                        nums.add(tmp);
                    }
                }
            }

            if (cur[1] == 0) {
                tmp = cur[0] / 2;
                if (!nums.contains(tmp)) {
                    if (tmp <= T) {
                        if (tmp == T) {
                            answer = T;
                            break;
                        } else {
                            q.add(new int[]{tmp, 1});
                            nums.add(tmp);
                        }
                    }
                }
            }
        }
        System.out.println(answer);
    }
}
