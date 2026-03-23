import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st;
        int total = 0;
        StringBuilder sb = new StringBuilder();

        for (int tc = 0; tc < N; tc++) {
            int L = Integer.parseInt(br.readLine());
            int[] arr = new int[L];
            st = new StringTokenizer(br.readLine());
            int max = 0, maxS = 0, maxE = 0;
            int start = 0, end = 0;

            for (int i = 0; i < L; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
                if (i == 0) {
                    max = arr[i];
                } else {
                    if (arr[i] >= arr[i-1] + arr[i]) {
                        start = i;
                        end = i;
                    } else {
                        arr[i] = arr[i-1] + arr[i];
                        end = i;
                    }

                    // 최대 값 비교
                    if (arr[i] > max) {
                        maxS = start;
                        maxE = end;
                        max = arr[i];
                    } else if (arr[i] == max && (maxE - maxS > end - start)) {
                        max = arr[i];
                        maxS = start;
                        maxE = end;
                    }
                }
            }
            total += max;
            sb.append(maxS+1).append(" ").append(maxE+1).append("\n");
        }
        System.out.println(total);
        System.out.print(sb);
    }
}
