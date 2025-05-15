import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] books = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());
            books[i] = num;
        }
        Arrays.sort(books);

        List<Integer> minus = new ArrayList<>();
        List<Integer> plus = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            if (books[i] < 0) {
                minus.add(books[i]);
            } else {
                plus.add(books[i]);
            }
        }
        Collections.sort(plus, Collections.reverseOrder());

        int ans = 0;
        for (int i = 0; i < minus.size(); i += M) {
            int tmp = 0;
            for (int j = 0; j < M; j++) {
                tmp = Math.max(tmp, Math.abs(minus.get(i)));
            }
            ans += tmp * 2;
        }

        for (int i = 0; i < plus.size(); i += M) {
            int tmp = 0;
            for (int j = 0; j < M; j++) {
                tmp = Math.max(tmp, plus.get(i));
            }
            ans += tmp * 2;

        }

        if (plus.size() > 0 && minus.size() > 0 ) {
            ans -= Math.max(Math.abs(minus.get(0)), plus.get(0));
        } else if (plus.size() > 0) {
            ans -= plus.get(0);
        } else if (minus.size() > 0) {
            ans -= Math.abs(minus.get(0));
        }

        System.out.print(ans);
    }

}
