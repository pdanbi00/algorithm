class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        int l1 = my_string.length();
        int l2 = overwrite_string.length();
        
        for (int i = 0; i < s; i++) {
            answer += my_string.charAt(i);
        }
        
        for (int i = 0; i < l2; i++) {
            answer += overwrite_string.charAt(i);
        }
        
        for (int i = l2+s; i < l1; i++) {
            answer += my_string.charAt(i);
        }
        return answer;
    }
}