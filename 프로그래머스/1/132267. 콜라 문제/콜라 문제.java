class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        while (n >= a) {
            int tmp = n / a;
            answer += tmp * b;
            
            n -= tmp * a;
            n += tmp * b;
        }
        return answer;
    }
}