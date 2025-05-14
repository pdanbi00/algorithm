class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        boolean possible;
        int cnt = 0;
        while (true) {
            int[] tmp = new int[arr.length];
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] >= 50 && arr[i] % 2 == 0) {
                    tmp[i] = arr[i] / 2;
                } else if (arr[i] < 50 && arr[i] % 2 == 1) {
                    tmp[i] = arr[i] * 2 + 1;
                } else {
                    tmp[i] = arr[i];
                }
            }
            possible = true;
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] != tmp[i]) {
                    possible = false;
                    break;
                }
            }
            
            if (possible) {
                answer = cnt;
                break;
            }
            cnt++;
            for (int i = 0; i < arr.length; i++) {
                arr[i] = tmp[i];
            }
            
        }
        
        
        return answer;
    }
}