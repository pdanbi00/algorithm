import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    static boolean check(int len, int num) {
        String tmp = String.valueOf(num);
        StringBuilder sbb = new StringBuilder();
        for (int i = 0; i < len-tmp.length(); i++) {
            sbb.append('0');
        }
        sbb.append(tmp);
        tmp = sbb.toString();

        for (int i = 0; i < len/2; i++) {
            if (tmp.charAt(i) != tmp.charAt(len-1-i)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        while (true) {
            String s = br.readLine();

            if (s.equals("0")) {
                break;
            }
            int len = s.length();
            int num = Integer.parseInt(s);
            int cnt = 0;
            while (!check(len, num+cnt)) {
                cnt++;
            }
            sb.append(cnt).append("\n");
        }
        System.out.print(sb);
    }
}
