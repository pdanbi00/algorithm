import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());

        List<int[]> schedule = new ArrayList<>();
        int[] arr;

        for (int i = 0; i < N; i++) {
            arr = new int[2];
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 2; j++) {
                arr[j] = Integer.parseInt(st.nextToken());
            }
            schedule.add(arr);
        }
        schedule.sort((a, b) -> {
            if (a[0] == b[0]) {
                return b[1] - a[1];
            }
            return a[0] - b[0];
        });

        int[] days = new int[366];

        for (int[] day : schedule) {
            for (int i = day[0]; i <= day[1]; i++) {
                days[i]++;
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
