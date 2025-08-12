import java.io.*;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int max_value = -1;
        int r = 0;
        int c = 0;

        for (int i = 0; i < 9; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 9; j++) {
                int num = Integer.parseInt(st.nextToken());
                if (num > max_value) {
                    max_value = num;
                    r = i + 1;
                    c = j + 1;
                }
            }
        }

        System.out.println(max_value);
        System.out.println(r + " " + c);
    }
}
