import java.util.ArrayList;
class Solution {
    public String[] solution(String my_str, int n) {
        String[] answer = {};
        int idx = 0;
        int N = my_str.length();
        ArrayList<String> arr = new ArrayList<>();
        
        while (idx < N) {
            String tmp = "";
            for (int i = 0; i < n; i++) {
                if (idx < N) {
                    tmp += my_str.charAt(idx);
                    idx++;
                }
            }
            arr.add(tmp);
        }
        
        answer = new String[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            answer[i] = arr.get(i);
        }
        return answer;
    }
}