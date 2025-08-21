import java.io.*;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.Collections;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int aCnt = Integer.parseInt(st.nextToken());
            Integer[] A = new Integer[aCnt];
            for (int j = 0; j < aCnt; j++) {
                A[j] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            int bCnt = Integer.parseInt(st.nextToken());
            Integer[] B = new Integer[bCnt];
            for (int j = 0; j < bCnt; j++) {
                B[j] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(A, Collections.reverseOrder());
            Arrays.sort(B, Collections.reverseOrder());

            int len = Math.min(aCnt, bCnt);
            boolean find = false;
            char answer = 'D';

            for (int j = 0; j < len; j++) {
                if (A[j] > B[j]) {
                    find = true;
                    answer = 'A';
                    break;
                } else if (A[j] < B[j]) {
                    find = true;
                    answer = 'B';
                    break;
                }
            }

            if (!find) {
                if (aCnt > bCnt) {
                    answer = 'A';
                } else if (aCnt < bCnt) {
                    answer = 'B';
                }
            }

            sb.append(answer + "\n");
        }
        System.out.println(sb);
    }
}
