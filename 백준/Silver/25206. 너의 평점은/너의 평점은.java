import java.io.*;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        double score = 0;
        double total = 0;
        StringTokenizer st;
        for (int i = 0; i < 20; i++) {
            st = new StringTokenizer(br.readLine());
            String subject = st.nextToken();
            double credit = Double.valueOf(st.nextToken());
            String grade = st.nextToken();
            if (!grade.equals("P")) {
                total += credit;
                if (grade.equals("A+")) {
                    score += credit * 4.5;
                } else if (grade.equals("A0")) {
                    score += credit * 4.0;
                } else if (grade.equals("B+")) {
                    score += credit * 3.5;
                } else if (grade.equals("B0")) {
                    score += credit * 3.0;
                } else if (grade.equals("C+")) {
                    score += credit * 2.5;
                } else if (grade.equals("C0")) {
                    score += credit * 2.0;
                } else if (grade.equals("D+")) {
                    score += credit * 1.5;
                } else if (grade.equals("D0")) {
                    score += credit * 1.0;
                } else if (grade.equals("F")) {
                    score += credit * 0.0;
                }
            }
        }
        System.out.printf("%.6f", score / total);
    }
}
