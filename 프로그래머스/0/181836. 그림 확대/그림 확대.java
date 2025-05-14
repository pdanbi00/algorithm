import java.util.*;
class Solution {
    public String[] solution(String[] picture, int k) {
        String[] answer = {};
        List<String> list = new ArrayList<>();
        for (int i = 0; i < picture.length; i++) {
            String tmp = "";
            for (int j = 0; j < picture[i].length(); j++) {
                for (int p = 0; p < k; p++) {
                    tmp += picture[i].charAt(j);
                }
            }
            for (int p = 0; p < k; p++) {
                list.add(tmp);
            }
            
        }
        answer = new String[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}