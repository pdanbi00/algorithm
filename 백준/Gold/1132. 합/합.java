import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long[] alpha = new long[10]; // A ~ J에 해당하는 값들의 총 합
        for (int i = 0; i < 10; i++) {
            alpha[i] = 0;
        }

        boolean[] zero = new boolean[10];
        for (int i = 0; i < 10; i++) {
            zero[i] = true;
        }

        for (int i = 0; i < N; i++) {
            String arr = br.readLine();
            // 뒤에서부터 확인
            for (int j = arr.length() - 1; j >= 0; j--) {
                alpha[(int) arr.charAt(j) - 65] += (long) Math.pow(10, ((arr.length()-1)-j));
            }
            zero[arr.charAt(0) - 65] = false; // 첫번째에 올 수 없는 값임을 표시

        }

        int cnt = 0;
        for (int i = 0; i < 10; i++) {
            if (alpha[i] > 0) {
                cnt++;
            }
        }

        if (cnt == 10) { // 0이 포함되어야 됨
            long min_val = Long.MAX_VALUE;
            int min_idx = -1;
            for (int i = 0; i < 10; i++) {
                if (zero[i] && (min_val > alpha[i])) {
                    min_val = alpha[i];
                    min_idx = i;
                }
            }

            // 어차피 0인 곳은 곱해도 0이니깐 alpha값을 0으로 변환
            alpha[min_idx] = 0;
        }

        long total = 0;
        Arrays.sort(alpha);

        for (int i = 9; i >= 0; i--) {
            total += alpha[i] * i;
        }
        System.out.print(total);

    }
}
