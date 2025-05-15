import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        int cnt = 0;
        for (int key : map.keySet()) {
            cnt += 1;
        }
        int n = nums.length;
        
        if (n / 2 >= cnt) {
            answer = cnt;
        } else {
            answer = n / 2;
        }
        
        return answer;
    }
}