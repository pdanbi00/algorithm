class Solution {
    public String solution(String my_string, int s, int e) {
        String answer = "";
        String tmp1 = my_string.substring(0, s);
        String tmp3 = my_string.substring(e+1);
        String tmp2 = "";
        for (int i = e; i >= s; i--) {
            tmp2 += my_string.charAt(i);
        }
        answer = tmp1 + tmp2 + tmp3;
        return answer;
    }
}