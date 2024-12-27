import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException{
        int N = Integer.parseInt(br.readLine());
        int[] snow = new int[N];

        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {
            snow[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(snow);

        int answer = Integer.MAX_VALUE;
        for (int i = 0; i < N-1; i++) {
            for (int j = i+1; j < N; j++) {
                int snowMan1 = snow[i] + snow[j];
                int left = 0, right = N-1;

                while (left < right && answer != 0) {
                    if (left == i || left == j) {
                        left++;
                        continue;
                    }
                    if (right == i || right == j) {
                        right--;
                        continue;
                    }
                    int snowMan2 = snow[left] + snow[right];
                    answer = Math.min(answer, Math.abs(snowMan1 - snowMan2));
                    if (snowMan1 > snowMan2) {
                        left++;
                    } else {
                        right--;
                    }
                }
                if (answer == 0){
                    break;
                }
            }
        }
        System.out.println(answer);

    }
}
