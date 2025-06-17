import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int D = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        int[] oven = new int[D];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < D; i++) {
            oven[i] = Integer.parseInt(st.nextToken());
        }

        // 오븐 정렬하기
        for (int i = 1; i < D; i++) {
            if (oven[i-1] < oven[i]) {
                oven[i] = oven[i-1];
            }
        }

        int[] pizza = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            pizza[i] = Integer.parseInt(st.nextToken());
        }

        int cnt = 0; // 오븐에 들어간 피자 개수
        int idx = D-1; // 오븐의 인덱스
        while (idx >= 0) {
            if (pizza[cnt] <= oven[idx]) {
                cnt++;
                if (cnt == N) {
                    break;
                }
            }
            idx--;
        }

        if (cnt == N) {
            System.out.println(idx+1);
        } else {
            System.out.println(0);
        }
    }
}
