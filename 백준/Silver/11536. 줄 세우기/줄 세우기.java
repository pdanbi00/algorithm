import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] names = new String[N];
        String[] sortedNames = new String[N];
        for (int i = 0; i < N; i++) {
            names[i] = sortedNames[i] = br.readLine();
        }

        Arrays.sort(sortedNames);

        boolean possible = true;
        // 오름차순 체크
        for (int i = 0; i < N; i++) {
            if (sortedNames[i] != names[i]) {
                possible = false;
                break;
            }
        }

        if (possible) {
            System.out.print("INCREASING");
        } else {
            Arrays.sort(sortedNames, Comparator.reverseOrder());

            possible = true;
            // 내림차순 체크
            for (int i = 0; i < N; i++) {
                if (sortedNames[i] != names[i]) {
                    possible = false;
                    break;
                }
            }
            if (possible) {
                System.out.print("DECREASING");
            } else {
                System.out.print("NEITHER");
            }
        }
    }
}
