class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        for (int i = 0; i < num_list.length; i++) {
            while (num_list[i] >= 1) {
                if (num_list[i] == 1) {
                    break;
                }
                if (num_list[i] % 2 == 1) {
                    num_list[i] -= 1;
                }
                num_list[i] /= 2;
                answer += 1;
            }
        }
        return answer;
    }
}