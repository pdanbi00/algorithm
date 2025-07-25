import java.io.*;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Collections;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<String, Integer> bookSale = new HashMap<>();
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String book = br.readLine();
            if (bookSale.containsKey(book)) {
                bookSale.put(book, bookSale.get(book) + 1);
            } else {
                bookSale.put(book, 1);
            }
        }
        int max_cnt = 0;
        ArrayList<String> books = new ArrayList<>();
        for (Entry<String, Integer> elem : bookSale.entrySet()) {
            String b = elem.getKey();
            int cnt = elem.getValue();
            if (cnt > max_cnt) {
                max_cnt = cnt;
                books = new ArrayList<>();
                books.add(b);
            } else if (cnt == max_cnt) {
                books.add(b);
            }
        }
        Collections.sort(books);
        System.out.println(books.get(0));
    }
}
