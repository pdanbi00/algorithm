import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st;

        int[] originPlus = new int[N];
        int[] originMinus = new int[N];

        int[] sortPlus = new int[N];
        int[] sortMinus = new int[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            originPlus[i] = a+b;
            originMinus[i] = a-b;

            sortPlus[i] = a+b;
            sortMinus[i] = a-b;
        }

        Arrays.sort(sortPlus);
        Arrays.sort(sortMinus);

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++) {

            // 최솟값
            int s = 0;
            int e = N-1;
            int mid;

            while (s <= e) {
                mid = (s + e) / 2;
                if (sortPlus[mid] >= originMinus[i]) {
                    e = mid - 1;
                } else {
                    s = mid + 1;
                }
            }
            sb.append(s+1).append(" ");

            // 최댓값
            s = 0;
            e = N-1;

            while (s <= e) {
                mid = (s + e) / 2;
                if (sortMinus[mid] <= originPlus[i]) {
                    s = mid + 1;
                } else {
                    e = mid - 1;
                }
            }
            sb.append(e+1).append("\n");
        }
        System.out.println(sb);
    }
}
