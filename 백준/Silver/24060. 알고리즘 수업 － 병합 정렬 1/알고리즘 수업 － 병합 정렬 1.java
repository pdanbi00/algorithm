import java.io.*;
import java.util.StringTokenizer;
public class Main {
    static int N, K;
    static int[] nums;
    static int result;
    static int cnt;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        nums = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        result = -1;
        merge_sort(0, N-1);
        System.out.println(result);
    }
    static public void merge_sort(int p, int r) {
        if (cnt > K) {
            return;
        }

        if (p < r) {
            int q = (p + r) / 2;
            merge_sort(p, q);
            merge_sort(q+1, r);
            merge(p, q, r);
        }
    }
    static public void merge(int p, int q, int r) {
        int i = p;
        int j = q + 1;
        int t = 0;
        int[] tmp = new int[r-p+1];
        while (i <= q & j <= r) {
            if (nums[i] <= nums[j]) {
                tmp[t++] = nums[i++];


            } else {
                tmp[t++] = nums[j++];
            }
        }

        while (i <= q) {
            tmp[t++] = nums[i++];
        }
        while (j <= r) {
            tmp[t++] = nums[j++];
        }
        i = p;
        t = 0;
        while (i <= r) {
            nums[i] = tmp[t];
            cnt++;
            if (cnt == K) {
                result = tmp[t];
                break;
            }
            t++;
            i++;
        }
    }
}
