import java.util.Arrays;
class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        Arrays.sort(A);
        Arrays.sort(B);
        
        int N = A.length;
        for (int i = 0; i < N; i++) {
            answer += A[i] * B[N-1-i];
        }
        
//         Arrays.sort(A, Comparator.reverseOrder());
//         Arrays.sort(B);
        
//         tmp = 0;
//         for (int i = 0; i < N; i++) {
//             tmp += A[i] * B[i];
//         }
//         answer = Math.min(answer, tmp);
        return answer;
    }
}