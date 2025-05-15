class Solution {
    public String solution(String number, int k) {
        String answer = "";
        int idx = 0;
        StringBuilder sb = new StringBuilder();
        // 앞에서부터 (전체길이 - k) 수 중 가장 큰 수 선택
        // 선택한 수 다음 인덱스부터 탐색범위 한칸씩 늘리면서 반복적으로 탐색
        for (int i = 0; i < number.length() - k; i++) {
            char max = 0;
            for (int j = idx; j <= i+k; j++) {
                if (max < number.charAt(j)) {
                    max = number.charAt(j);
                        idx = j + 1;
                }
            }
            sb.append(max);
        }
        return sb.toString();
    }
}