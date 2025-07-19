import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        for (int i = 1; i <= 5; i++) {
            String name = br.readLine();
            if (name.contains("FBI")) {
                cnt++;
                sb.append(i).append(" ");
            }
        }
        if (cnt == 0) {
            sb.append("HE GOT AWAY!");
        }
        System.out.println(sb);
    }
}
