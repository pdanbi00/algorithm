class Solution {
    public int solution(int M, int N) {
        int answer = M-1;
        answer += M * (N-1);
        return answer;
    }
}