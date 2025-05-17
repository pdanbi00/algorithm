import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        List<Integer> list = new ArrayList<>();
        for (int i = 1; i <= N; i++) {
            list.add(i);
        }

        while (!list.isEmpty()) {
            System.out.print(list.remove(0) + " ");
            if (!list.isEmpty()) {
                int tmp = list.remove(0);
                list.add(tmp);
            }

        }
    }
}
