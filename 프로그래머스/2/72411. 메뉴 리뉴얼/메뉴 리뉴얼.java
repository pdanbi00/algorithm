import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

class Solution {
    static ArrayList<String> answerList = new ArrayList<>();
    static Map<String, Integer> map = new HashMap<>();
    
    public String[] solution(String[] orders, int[] course) {
        String[] answer = {};
        
        String[] newOrders = new String[orders.length];
        for (int i = 0; i < orders.length; i++) {
            char[] tmp = orders[i].toCharArray();
            Arrays.sort(tmp);
            newOrders[i] = new String(tmp);
        }
        
        for (int cnt : course) {
            for (String order : newOrders) {
                dfs(0, "", order, cnt);
            }
            
            if (!map.isEmpty()) {
                ArrayList<Integer> countList = new ArrayList<>(map.values());
                int max = Collections.max(countList);
                if (max > 1) {
                    for (String key : map.keySet()) {
                        if (map.get(key) == max) {
                            answerList.add(key);
                        }
                    }
                }
            }
            map.clear();
        }
        Collections.sort(answerList);
        answer = new String[answerList.size()];
        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }
        
        return answer;
    }
    
    static void dfs(int depth, String course, String chars, int total) {
        if (course.length() == total) {
            map.put(course, map.getOrDefault(course, 0) + 1);
            return;
        }
        
        if (depth >= chars.length()) {
            return;
        }
        
        dfs(depth+1, course, chars, total);
        dfs(depth+1, course + chars.charAt(depth), chars, total);
    }
}