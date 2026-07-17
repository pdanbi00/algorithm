class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        int answer = 0;
        
        int gcdA = arrayA[0];
        int gcdB = arrayB[0];
        
        for (int i = 1; i < arrayA.length; i++) {
            gcdA = gcd(gcdA, arrayA[i]);
            gcdB = gcd(gcdB, arrayB[i]);
        }
        
        for (int i = 0; i < arrayB.length; i++) {
            if (arrayB[i] % gcdA == 0) {
                gcdA = 0;
                break;
            }
        }
        
        for (int i = 0; i < arrayA.length; i++) {
            if (arrayA[i] % gcdB == 0) {
                gcdB = 0;
                break;
            }
        }
        
        return Math.max(gcdA, gcdB);
    }
    
    public int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }
}