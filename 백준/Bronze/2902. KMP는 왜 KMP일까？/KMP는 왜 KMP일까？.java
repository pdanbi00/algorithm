import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        StringTokenizer st = new StringTokenizer(line, "-");
        StringBuilder sb = new StringBuilder();
        while (st.hasMoreTokens()) {
            sb.append(st.nextToken().charAt(0));
        }
        System.out.print(sb);
    }
}
