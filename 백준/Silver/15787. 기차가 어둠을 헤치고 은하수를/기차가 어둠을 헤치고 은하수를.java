import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] train = new int[N][20];

        int a, b, c;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            if (a == 1) {
                b = Integer.parseInt(st.nextToken());
                c = Integer.parseInt(st.nextToken());
                train[b-1][c-1] = 1;
            } else if (a == 2) {
                b = Integer.parseInt(st.nextToken());
                c = Integer.parseInt(st.nextToken());
                train[b-1][c-1] = 0;
            } else if (a == 3) {
                b = Integer.parseInt(st.nextToken());
                train[b-1][19] = 0;
                for (int j = 18; j >= 0; j--) {
                    train[b-1][j+1] = train[b-1][j];
                }
                train[b-1][0] = 0;
            } else {
                b = Integer.parseInt(st.nextToken());
                train[b-1][0] = 0;
                for (int j = 0; j < 19; j++) {
                    train[b-1][j] = train[b-1][j+1];
                }
                train[b-1][19] = 0;
            }
        }
        Set<List<Integer>> milkyWay = new HashSet<>();
        for (int i = 0; i < N; i++) {
            List<Integer> list = new ArrayList<>();
            for (int j = 0; j < 20; j++) {
                list.add(train[i][j]);
            }
            milkyWay.add(list);
        }
        System.out.print(milkyWay.size());
    }
}
