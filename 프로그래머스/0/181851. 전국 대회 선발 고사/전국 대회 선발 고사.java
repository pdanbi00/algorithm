import java.util.*;

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        int answer = 0;
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < rank.length; i++) {
            if (attendance[i]) {
                map.put(rank[i], i);
            }
        }
        List<Integer> keyList = new ArrayList<>(map.keySet());
        List<Integer> valueList = new ArrayList<>();
        Collections.sort(keyList);
        
        int a = 0;
        for (int i = 0; i < keyList.size(); i++) {
            a = keyList.get(i);
            valueList.add(map.get(a));
        }
        answer = valueList.get(0) * 10000 + valueList.get(1) * 100 + valueList.get(2);
        return answer;
    }
}