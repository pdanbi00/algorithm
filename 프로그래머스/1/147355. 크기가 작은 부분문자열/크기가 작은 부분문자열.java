class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int N = t.length();
        int M = p.length();
        long num = Long.valueOf(p);
        
        for (int i = 0; i < N-M+1; i++) {
            String tmp = t.substring(i, i+M);
            long tmpNum = Long.valueOf(tmp);
            if (tmpNum <= num) {
                answer++;
            }
        }
        return answer;
    }
}