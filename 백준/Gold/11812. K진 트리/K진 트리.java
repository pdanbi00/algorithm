import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        // N의 범위가 10 ^ 15이기 때문에 int 타입이 아니고 long 타입
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long N = Long.parseLong(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int Q = Integer.parseInt(st.nextToken());

        StringBuilder sb = new StringBuilder();
        while (Q-- > 0) {
            st = new StringTokenizer(br.readLine());
            long A = Long.parseLong(st.nextToken());
            long B = Long.parseLong(st.nextToken());

            if (K==1) {
                sb.append(Math.abs(A-B)).append("\n");
            } else {
                int cnt = 0;
                while (A != B) {
                    if (A > B) {
                        A = (A-2) / K + 1;
                    } else {
                        B = (B-2) / K + 1;
                    }
                    cnt ++;
                }
                sb.append(cnt).append("\n");

            }
        }
        System.out.print(sb.toString().trim());

    }
}
