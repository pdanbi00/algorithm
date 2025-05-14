class Solution {
    public String solution(String my_string, int[][] queries) {
        for (int i = 0; i < queries.length; i++) {
            int s = queries[i][0], e = queries[i][1];
            String tmp1 = my_string.substring(0, s);
            String tmp2 = my_string.substring(s, e+1);
            String tmp3 = my_string.substring(e+1, my_string.length());
            StringBuffer sb = new StringBuffer(tmp2);
            tmp2 = sb.reverse().toString();
            my_string = tmp1 + tmp2 + tmp3;
            
        }
        return my_string;
    }
}