class Solution {
    public String solution(String s, int n) {
        String answer = "";
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                answer += " ";
                continue;
            }
            
            int tmp = (int) s.charAt(i);
            if (tmp >= 65 && tmp <= 90) {
                tmp += n;
                if (tmp > 90) {
                    tmp -= 90;
                    tmp += 64;
                }
                
            } else if (tmp >= 97 && tmp <= 122) {
                tmp += n;
                if (tmp > 122) {
                    tmp -= 122;
                    tmp += 96;
                }
            }
            
            answer += (char) tmp;
        }
        return answer;
    }
}