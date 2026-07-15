class Solution
{
    public int solution(String s)
    {
        int answer = 1;
        int N = s.length();

        int[][] dp = new int[N][N];
        for (int i = 0; i < N; i++) {
            dp[i][i] = 1;
        }
        
        for (int i = 0; i < N-1; i++) {
            if (s.charAt(i) == s.charAt(i+1)) {
                dp[i][i+1] = 1;
                answer = 2;
            }
        }
        
        // dp[i][j] : i번째 문자부터 j번째 문자까지 팰린드롬인지 여부
        // s[i] == s[j] 이면 dp[i+1][j-1]이 팰린드롬일 경우 팰린드롬 맞음
        // 길이를 가장 바깥에
        
        for (int k = 2; k < N; k++) {
            for (int i = 0; i < N-k; i++) {
                int j = i + k;
                if (s.charAt(i) == s.charAt(j) && dp[i+1][j-1] == 1) {
                    dp[i][j] = 1;
                    answer = Math.max(answer, j - i + 1);
                }
            }
        }
        
        

        return answer;
    }
}