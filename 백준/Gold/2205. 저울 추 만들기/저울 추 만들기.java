import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer> check = new ArrayList<>();

        int idx = 2;
        while (true) {
            if (idx <= 2 * N) {
                check.add(idx);
            } else {
                break;
            }
            idx *= 2;
        }

        int[] weight = new int[N+1];

        for (int i = N; i > 0; i--) {
            for (int k : check) {
                if (k - i <= N && k > i) {
                    if (weight[i] == 0 && weight[k-i] == 0) {
                        weight[i] = k-i;
                        weight[k-i] = i;
                    }
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            sb.append(weight[i]).append("\n");
        }
        System.out.print(sb);
    }
}
