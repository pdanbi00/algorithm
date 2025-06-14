import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[] hills;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        hills = new int[N];
        int max = -1;
        int min = 101;
        for (int i = 0; i < N; i++) {
            hills[i] = Integer.parseInt(br.readLine());
            if (hills[i] > max) {
                max = hills[i];
            }

            if (hills[i] < min) {
                min = hills[i];
            }
        }

        int answer = Integer.MAX_VALUE;
        for (int tmp = min; tmp <= max-17; tmp++) {
            int result = 0;
            for (int i = 0; i < N; i++) {
                if (hills[i] < tmp) {
                    result += Math.pow((tmp - hills[i]), 2);
                } else if (hills[i] > tmp + 17) {
                    result += Math.pow((hills[i] - (tmp + 17)), 2);
                }
            }
//            System.out.println("tmp : " + tmp + " result : " + result);
            if (answer > result) {
                answer = result;
            }
        }
        if (answer == Integer.MAX_VALUE) {
            System.out.println(0);
        } else {
            System.out.println(answer);
        }



    }
}
