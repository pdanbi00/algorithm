import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();

        String temp = line.substring(0, 1);
        // 사전 반대 순으로 먼저 나열
        for (int i = 1; i < line.length(); i++) {
            if (temp.charAt(i-1) < line.charAt(i)) {
                temp = line.charAt(i) + temp;
            } else {
                temp = temp + line.charAt(i);
            }
        }

        // 최종적으로 만들어진 문자열을 뒤집어서 사전 순으로 나열
        String ans = "";
        for (int i = temp.length() - 1; i >= 0; i--) {
            ans += temp.charAt(i);
        }
        System.out.print(ans);
    }
}
