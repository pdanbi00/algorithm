class Solution {
    public String[] solution(String[] str_list) {
        String[] answer = {};
        int l_idx = 30, r_idx = 30;
        for (int i = 0; i < str_list.length; i++) {
            if (l_idx == 30 && str_list[i].equals("l")) {
                l_idx = i;
            }
            if (r_idx == 30 && str_list[i].equals("r")) {
                r_idx = i;
            }
        }
        
        if (l_idx < r_idx) {
            answer = new String[l_idx];
            for (int i = 0; i < l_idx; i++) {
                answer[i] = str_list[i];
            }
        } else if (l_idx > r_idx) {
            answer = new String[str_list.length - r_idx - 1];
            for (int i = r_idx+1; i < str_list.length; i++) {
                answer[i-(r_idx+1)] = str_list[i];
            }
        }
        return answer;
    }
}