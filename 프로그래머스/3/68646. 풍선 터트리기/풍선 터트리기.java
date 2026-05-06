class Solution {
    public int solution(int[] a) {
        int answer = 0;
        int N = a.length;
        
        int[] prefixMin = new int[N]; // 0부터 i번째까지의 최소값
        int[] suffixMin = new int[N]; // i부터 N-1까지의 최소값
        
        prefixMin[0] = a[0];
        
        for (int i = 1; i < N;i ++) {
            prefixMin[i] = Math.min(prefixMin[i-1], a[i]);
        }
        
        suffixMin[N-1] = a[N-1];
        for (int i = N-2; i >= 0; i--) {
            suffixMin[i] = Math.min(suffixMin[i+1], a[i]);
        }
        
        for (int i = 0; i < N; i++) {
            if (a[i] == prefixMin[i] || a[i] == suffixMin[i]) { // a[i]가 양 쪽 모두 보다 크면 안됨 즉, 양 쪽 중 한쪽 이상의 최솟값이 a[i]보다 크면 가능
                answer++;
            }
        }
        return answer;
    }
}