import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String arr = br.readLine();

        int N = arr.length();
        boolean possible = true;

        for (int i = 0; i < N/2; i++) {
            if (arr.charAt(i) != arr.charAt(N-1-i)) {
                possible = false;
                break;
            }
        }
        if (possible) {
            System.out.print("true");
        } else {
            System.out.print("false");
        }
    }
}