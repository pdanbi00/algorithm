import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Long N = Long.parseLong(br.readLine());

        if (N % 7 == 2 || N % 7 == 0) {
            System.out.print("CY");
        } else {
            System.out.print("SK");
        }
    }
}
