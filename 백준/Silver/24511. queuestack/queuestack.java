import java.io.*;
import java.util.StringTokenizer;
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] A = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        int zeroCnt = 0;
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
            if (A[i] == 0) {
                zeroCnt++;
            }
        }

        int[] B = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }

        ArrayList<Integer> answer = new ArrayList<>();
        if (zeroCnt > 0) {
            for (int i = N-1; i >= 0; i--) {
                if (A[i] == 0) {
                    answer.add(B[i]);
                }
            }
        }
        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            answer.add(Integer.parseInt(st.nextToken()));
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            sb.append(answer.get(i)).append(" ");
        }
        System.out.println(sb);

    }
}
