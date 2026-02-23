import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        String[] arr = line.split("-");
        String answer = "";
        for (String a : arr) {
            answer += a.charAt(0);
        }
        System.out.print(answer);
    }
}
