class Solution {
    public String solution(int n, int t, int m, int p) {
        String answer = "";
        String tmp = "";
        for (int i = 0; i <= (m * t); i++) {
            tmp += Integer.toString(i, n);
        }

        
        for (int i = 0; i < t; i++) {
            char c = tmp.charAt(p-1 + (m*i));
            if (!Character.isDigit(c)) {
                answer += Character.toUpperCase(c);
            } else {
                answer += c;
            }
        }
        
        return answer;
    }
}