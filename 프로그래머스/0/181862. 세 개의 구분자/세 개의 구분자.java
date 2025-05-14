class Solution {
    public String[] solution(String myStr) {
        String[] answer = {};
        String tmp = myStr.replaceAll("[a-c]", " ");
        answer = tmp.trim().split("\\s+");
        if (answer[0].isEmpty()) {
            answer[0] = "EMPTY";
        }
        return answer;
    }
}