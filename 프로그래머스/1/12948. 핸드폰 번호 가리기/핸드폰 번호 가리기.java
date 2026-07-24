class Solution {
    public String solution(String phone_number) {
        String answer = "";
        int n = phone_number.length();
        for (int i = 0; i < n; i++) {
            if (i < n-4) {
                answer += "*";
            } else {
                answer += phone_number.charAt(i);
            }
            
        }
        return answer;
    }
}