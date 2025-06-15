import java.util.*;
import java.io.*;
public class Main {
    static int chu_cnt;
    static int[] chu_list;
    static boolean[][] dp;
    public static void main(String[] args) throws IOException{
        // dp[i][j] : i개의 추를 사용해서 j라는 무게를 만듦
        // 즉, dp[사용한 추의 개수][양쪽 저울의 추 무게의 차이]

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        chu_cnt = Integer.parseInt(br.readLine());
        chu_list = new int[chu_cnt];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < chu_cnt; i++) {
            chu_list[i] = Integer.parseInt(st.nextToken());
        }


        dp = new boolean[chu_cnt+1][40001];

        calc(0, 0);

        int bead_cnt = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < bead_cnt; i++) {
            int bead = Integer.parseInt(st.nextToken());
            if (dp[chu_cnt][bead]) {
                System.out.print("Y ");
            } else {
                System.out.print("N ");
            }
        }

    }

    static void calc(int cnt, int weight) {
        if (dp[cnt][weight]) {
            return;
        }

        dp[cnt][weight] = true;

        if (cnt == chu_cnt) {
            return;

        }

        // 추를 저울 오른쪽에 올리는 경우
        calc(cnt+1, weight + chu_list[cnt]);
        // 추를 저울 왼쪽에 올리는 경우
        calc(cnt+1, Math.abs(weight - chu_list[cnt]));
        // 추를 안 올리는 경우
        calc(cnt+1, weight);
    }

}