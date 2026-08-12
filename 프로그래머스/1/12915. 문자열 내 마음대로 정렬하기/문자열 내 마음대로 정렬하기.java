import java.util.ArrayList;
import java.util.Collections;
class Solution {
    public String[] solution(String[] strings, int n) {
        ArrayList<String> tmp = new ArrayList<>();
        for (int i = 0; i < strings.length; i++) {
            tmp.add(strings[i]);
        }
        Collections.sort(tmp);
        Collections.sort(tmp, (o1, o2) -> (o1.charAt(n) - o2.charAt(n)));
        String[] answer = new String[strings.length];
        for (int i = 0; i < strings.length; i++) {
            answer[i] = tmp.get(i);
        }
        return answer;
    }
}