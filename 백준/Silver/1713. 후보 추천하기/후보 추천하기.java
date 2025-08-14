import java.io.*;
import java.util.StringTokenizer;
import java.util.Collections;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int total = Integer.parseInt(br.readLine());

        List<Student> photos = new ArrayList<>();
        Student[] students = new Student[101];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < total; i++) {
            int num = Integer.parseInt(st.nextToken());

            // 사진 추가하기
            if (students[num] != null) {
                // 이미 사진틀 존재하는 경우
                students[num].cnt++;
            } else { // 사진틀 존재하지 않는 경우
                // 사진 틀 꽉 찬 경우
                Collections.sort(photos);

                if (photos.size() == N) {
                    // 사진 삭제
                    Student dell = photos.remove(0);
                    students[dell.num] = null;
                }

                students[num] = new Student(num, 1, i);
                photos.add(students[num]);
            }
        }

        // photos 출력
        Collections.sort(photos, (o1, o2) -> o1.num - o2.num);
        for (Student s : photos) {
            System.out.print(s.num + " ");
        }
    }
}

class Student implements Comparable<Student> {
    int num;
    int cnt;
    int time;

    public Student(int num, int cnt, int time) {
        this.num = num;
        this.cnt = cnt;
        this.time = time;
    }

    @Override
    public int compareTo(Student s2) {
        if (cnt == s2.cnt) {
            return time-s2.time;
        }
        return cnt - s2.cnt;
    }
}
