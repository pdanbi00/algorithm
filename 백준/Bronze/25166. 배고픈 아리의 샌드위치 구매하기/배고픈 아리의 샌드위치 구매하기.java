import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int S = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        if (S <= 1023) {
            System.out.print("No thanks");
        } else {
            if (((S - 1023) & M) == (S - 1023)) {
                System.out.print("Thanks");
            } else {
                System.out.print("Impossible");
            }
        }
    }
}
