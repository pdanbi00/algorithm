import java.util.*;
import java.io.*;
public class Main {
    public static boolean isPrime(int x) {
        if (x == 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(x); i++) {
            if (x % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());

            int a = N / 2;
            int b = N / 2;

            while (a > 0) {
                if (isPrime(a) && isPrime(b)) {
                    System.out.println(a + " " + b);
                    break;
                } else {
                    a -= 1;
                    b += 1;
                }
            }

        }

    }
}
