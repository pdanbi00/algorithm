import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        int s, e;
        int[] days = new int[366];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            s = Integer.parseInt(st.nextToken());
            e = Integer.parseInt(st.nextToken());
            for (int j = s; j <= e; j++) {
                days[j]++;
            }
        }

        int answer = 0;
        int day = 0;
        int pre = -1;
        int maxCnt = 0;

        while (day <= 365) {
            if (days[day] > 0) {
                if (pre == -1) {
                    pre = day;
                    maxCnt = days[day];
                } else {
                    maxCnt = Math.max(maxCnt, days[day]);
                }
            } else {
                if (pre != -1) {
                    answer += (day - pre) * maxCnt;
                    pre = -1;
                    maxCnt = 0;
                }
            }

            day++;
        }

        if (days[365] > 0) {
            answer += (day - pre) * maxCnt;
        }

        System.out.println(answer);
    }
}