class Solution {
    public String solution(String myString) {
        String answer = "";
        for (int i = 0; i < myString.length(); i++) {
            if ('l' - myString.charAt(i) > 0) {
                answer += 'l';
            } else {
                answer += myString.charAt(i);
            }
        }
        return answer;
    }
}