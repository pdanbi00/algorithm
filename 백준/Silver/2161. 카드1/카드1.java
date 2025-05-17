import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            q.add(i);
        }

        while (q.size() != 1) {
            System.out.print(q.poll() + " ");
            int tmp = q.poll();
            q.add(tmp);
        }
        System.out.print(q.poll());
    }
}
