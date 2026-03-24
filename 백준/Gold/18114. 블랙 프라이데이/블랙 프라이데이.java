import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    static int N, C;
    static int[] weight;
    static boolean binarySearch(int start, int end, int diff) {
        while (start <= end) {
            int mid = (start + end) / 2;
            if (weight[mid] > diff) {
                end = mid - 1;
            } else if (weight[mid] == diff) {
                return true;
            } else {
                start = mid + 1;
            }
        }
        return false;
    }

    static boolean check(int n, int c) {
        int i = 0, j = n-1;
        while (i < j) {
            int total = weight[i] + weight[j];
            if (total > c) {
                j -= 1;
            } else if (total == c) {
                return true;
            } else {
                int dif = c - total;
                if (binarySearch(i+1, j-1, dif)) {
                    return true;
                }
                i += 1;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        boolean possible = false;
        N = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        weight = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            weight[i] = Integer.parseInt(st.nextToken());
            if (weight[i] == C) {
                possible = true;
            }
        }
        Arrays.sort(weight);
        if (!possible) {
            possible = check(N, C);
            if (possible) {
                System.out.print(1);
            } else {
                System.out.print(0);
            }
        } else {
            System.out.print(1);
        }
    }
}
