import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int J = Integer.parseInt(br.readLine());
        int S = J;

        int[] stock = new int[14];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 14; i++) {
            stock[i] = Integer.parseInt(st.nextToken());
        }

        int stockJ = 0, stockS = 0;

        // 준현이
        for (int i = 0; i < 14; i++) {
            if (J > 0) {
                stockJ += J / stock[i];
                J = J % stock[i];
            }
        }
        J += stockJ * stock[13];

        // 성민이
        int cnt = 0;
        for (int i = 3; i < 14; i++) {
            // 3일 연속 상승인지 확인
            cnt = 0;
            for (int j = 3; j > 0; j--) {
                if (stock[i-j] < stock[i-j+1]) {
                    cnt++;
                }
            }
            if (cnt == 3 && stockS > 0) {
                S += stockS * stock[i];
                stockS = 0;
            }

            // 3일 연속 하락인지 확인
            cnt = 0;
            for (int j = 3; j > 0; j--) {
                if (stock[i-j] > stock[i-j+1]) {
                    cnt++;
                }
            }
            if (cnt == 3 && S > 0) {
                stockS = S / stock[i];
                S = S % stock[i];

            }
        }
        S += stockS * stock[13];

        if (S == J) {
            System.out.println("SAMESAME");
        } else if (S > J) {
            System.out.println("TIMING");
        } else {
            System.out.println("BNP");
        }
    }
}
