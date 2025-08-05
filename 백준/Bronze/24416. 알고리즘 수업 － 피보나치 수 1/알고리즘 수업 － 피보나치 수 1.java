import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        System.out.println(fib(N) + " " + fibonachi(N));
    }

    static int fib(int n) {
        int[] f = new int[n+1];
        f[1] = 1;
        f[2] = 1;
        for (int i = 3; i <= n; i++) {
            f[i] = f[i-2] + f[i-1];
        }
        return f[n];
    }

    static int fibonachi(int n) {
        return n-2;
    }
}
