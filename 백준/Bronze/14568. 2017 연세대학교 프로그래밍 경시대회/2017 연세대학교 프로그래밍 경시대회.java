import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Set;
import java.util.List;
import java.util.HashSet;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Set<List<Integer>> answer = new HashSet<>();
        for (int a = 2; a < N-1; a += 2) {
            int tmp = N - a;
            for (int k = 2; k < tmp; k++) {
                if ((tmp - k) % 2 == 0) {
                    int b = (tmp - k) / 2;
                    if (b > 0) {
                        int c = b + k;
                        answer.add(Arrays.asList(a, b, c));
                    }
                }
            }
        }
        System.out.print(answer.size());
    }
}
