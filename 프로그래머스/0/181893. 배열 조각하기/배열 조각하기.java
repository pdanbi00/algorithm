import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] query) {
        for (int i = 0; i < query.length; i++) {
            List<Integer> list = new ArrayList<>();
            if (i % 2 == 0) {
                for (int j = 0; j <= query[i]; j++) {
                    list.add(arr[j]);
                }
            } else {
                for (int j = query[i]; j < arr.length; j++) {
                    list.add(arr[j]);
                }
            }
            arr = new int[list.size()];
            for (int j = 0; j < arr.length; j++) {
                arr[j] = list.get(j);
            }
        }
        return arr;
    }
}