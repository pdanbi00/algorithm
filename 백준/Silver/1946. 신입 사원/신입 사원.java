import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            int[][] scores = new int[N][2];

            for (int i = 0; i < N; i++) {
                String[] arr = br.readLine().split(" ");
                scores[i][0] = Integer.parseInt(arr[0]);
                scores[i][1] = Integer.parseInt(arr[1]);
            }

            // 서류 등수 순으로 정렬
            Arrays.sort(scores, new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    return Integer.compare(o1[0], o2[0]);
                }
            });

            int top = scores[0][1];
            int cnt = 1;
            for (int i = 1; i < N; i++) {
                if (top > scores[i][1]) {
                    cnt++;
                    top = scores[i][1];
                }
            }
            System.out.println(cnt);
        }

    }
}
