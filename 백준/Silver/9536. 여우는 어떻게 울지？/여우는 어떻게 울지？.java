import java.io.*;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < T; tc++) {
            st = new StringTokenizer(br.readLine());
            ArrayList<String> crying = new ArrayList<>();
            while (st.hasMoreTokens()) {
                crying.add(st.nextToken());
            }

            while (true) {
                String tmp = br.readLine();
                if (tmp.equals("what does the fox say?")) {
                    break;
                }
                String[] arr = tmp.split(" ");
                while (crying.contains(arr[2])) {
                    crying.remove(arr[2]);
                }
            }

            for (String word : crying) {
                sb.append(word + " ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
