import java.io.*;
import java.math.BigInteger;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BigInteger N = new BigInteger(br.readLine());
        BigInteger result = N.add(N).subtract(BigInteger.valueOf(2)); // N + N - 2를 이렇게 표현함...
        if (N.equals(BigInteger.ONE)) {
            result = BigInteger.ONE;
        }
        System.out.println(result);
    }
}
