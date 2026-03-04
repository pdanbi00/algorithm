import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        String n = String.valueOf(N);
        for (int i = 1; i <= N; i++) {
            sb.append(i);
        }
        System.out.print(sb.toString().indexOf(n)+1);
    }
}
