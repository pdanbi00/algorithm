import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken());
        int G = Integer.parseInt(st.nextToken());

        int tmp = gcd(R, G);

        List<Integer> answer = new ArrayList<>();
        for (int i = 1; i <= (int) Math.sqrt(tmp); i++) {
            if (tmp % i == 0) {
                answer.add(i);
                if (tmp / i == i) {
                    continue;
                }
                answer.add(tmp / i);
            }
        }

        for (int i = 0; i < answer.size(); i++) {
            int num = answer.get(i);
            System.out.println(num + " " + (R / num) + " " + (G / num));
        }
    }

    static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }
}
