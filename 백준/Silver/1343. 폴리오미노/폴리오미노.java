import java.io.*;
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String arr = br.readLine();
        ArrayList<Character> answer = new ArrayList<>();
        boolean possible = true;
        int idx = 0;

        while (idx < arr.length()) {
            if (arr.charAt(idx) == '.') {
                answer.add('.');
                idx++;
            } else if (idx <= arr.length()-4 && arr.charAt(idx) == 'X' && arr.charAt(idx+1) == 'X' && arr.charAt(idx+2) == 'X' && arr.charAt(idx+3) == 'X') {
                for (int i = 0; i < 4; i++) {
                    answer.add('A');
                }
                idx += 4;
            } else if (idx <= arr.length()-2 && arr.charAt(idx) == 'X' && arr.charAt(idx+1) == 'X') {
                for (int i = 0; i < 2; i++) {
                    answer.add('B');
                }
                idx += 2;
            } else {
                possible = false;
                break;
            }
        }
        StringBuilder sb = new StringBuilder();

        if (!possible) {
            System.out.println("-1");
        } else {
            for (int i = 0; i < answer.size(); i++) {
                sb.append(answer.get(i));
            }
            System.out.println(sb);
        }
    }


}
