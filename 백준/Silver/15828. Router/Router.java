import java.io.*;
import java.util.Deque;
import java.util.ArrayDeque;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Deque<Integer> router = new ArrayDeque<>();

        while (true) {
            int num = Integer.parseInt(br.readLine());
            if (num == -1) {
                break;
            } else if (num == 0) {
                router.pollFirst();
            } else {
                if (router.size() < N) {
                    router.addLast(num);
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        if (router.isEmpty()) {
            System.out.println("empty");
        } else {
            while (!router.isEmpty()) {
                sb.append(router.pollFirst()).append(" ");
            }
            System.out.println(sb);
        }

    }
}
