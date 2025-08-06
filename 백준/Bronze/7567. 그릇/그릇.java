import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String arr = br.readLine();
        int answer = 10;
        int idx = 1;
        char pre = arr.charAt(0);
        while (idx < arr.length()) {
            if (arr.charAt(idx) == pre) {
                answer += 5;
                idx += 1;
            } else {
                answer += 10;
                pre = arr.charAt(idx);
                idx += 1;
            }
        }
        System.out.println(answer);
    }
}
